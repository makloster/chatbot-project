from fastapi import FastAPI, HTTPException, Depends, Query
from typing import List, Optional
from pydantic import BaseModel
from passlib.context import CryptContext
import jwt
from datetime import datetime, timedelta, timezone

# ==============================
# 🔐 Configuración y Seguridad
# ==============================

SECRET_KEY = "mi_clave_secreta"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
fake_db = {"users": {}}

app = FastAPI()

# ====================
# 📦 Modelos de datos
# ====================


class UserRegister(BaseModel):
    username: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


class Payload(BaseModel):
    numbers: List[int]


class BinarySearchPayload(BaseModel):
    numbers: List[int]
    target: int


# =====================
# 🔐 Utilidades de auth
# =====================


def create_access_token(
    data: dict,
    expires_delta: timedelta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def authenticate_user(username: str, password: str):
    user = fake_db["users"].get(username)
    if user and verify_password(password, user["password"]):
        return username
    return None


def get_current_user(token: Optional[str] = Query(None)):
    if token is None:
        raise HTTPException(status_code=401, detail="Token no proporcionado")
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None or username not in fake_db["users"]:
            raise HTTPException(status_code=401, detail="Token inválido")
        return username
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expirado")
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Token inválido")


# ============================
# 🚪 Endpoints de autenticación
# ============================


@app.post("/register")
async def register(user: UserRegister):
    if user.username in fake_db["users"]:
        raise HTTPException(status_code=400, detail="El usuario ya existe")
    hashed_password = get_password_hash(user.password)
    fake_db["users"][user.username] = {"password": hashed_password}
    return {"message": "User registered successfully"}


@app.post("/login")
async def login(user: UserLogin):
    authenticated = authenticate_user(user.username, user.password)
    if not authenticated:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    token = create_access_token(data={"sub": user.username})
    return {"access_token": token}


# ======================
# 📊 Endpoints protegidos
# ======================


@app.post("/bubble-sort")
async def bubble_sort_endpoint(
    payload: Payload, username: str = Depends(get_current_user)
):
    sorted_numbers = bubble_sort(payload.numbers)
    return {"numbers": sorted_numbers}


@app.post("/filter-even")
async def filter_even_numbers(
    payload: Payload, username: str = Depends(get_current_user)
):
    even_numbers = [num for num in payload.numbers if num % 2 == 0]
    return {"even_numbers": even_numbers}


@app.post("/sum-elements")
async def sum_elements(payload: Payload, username: str = Depends(get_current_user)):
    total_sum = sum(payload.numbers)
    return {"sum": total_sum}


@app.post("/max-value")
async def max_value(payload: Payload, username: str = Depends(get_current_user)):
    if not payload.numbers:
        raise HTTPException(
            status_code=400, detail="La lista de números no puede estar vacía."
        )
    return {"max": max(payload.numbers)}


@app.post("/binary-search")
async def binary_search_endpoint(
    payload: BinarySearchPayload, username: str = Depends(get_current_user)
):
    sorted_numbers = bubble_sort(payload.numbers)
    found, index = binary_search(sorted_numbers, payload.target)
    return {"found": found, "index": index}


@app.post("/merge-sort")
async def merge_sort_endpoint(payload: Payload, username: str = Depends(get_current_user)):
    sorted_numbers = merge_sort(payload.numbers)
    return {"numbers": sorted_numbers}


@app.post("/min-value")
async def min_value(payload: Payload, username: str = Depends(get_current_user)):
    if not payload.numbers:
        raise HTTPException(status_code=400, detail="La lista no puede estar vacía.")
    return {"min": find_min(payload.numbers)}


@app.post("/mean-median")
async def mean_median(payload: Payload, username: str = Depends(get_current_user)):
    if not payload.numbers:
        raise HTTPException(status_code=400, detail="La lista no puede estar vacía.")
    return calculate_mean_median(payload.numbers)


# ===================
# 🔧 Algoritmos útiles
# ===================


def bubble_sort(arr: List[int]) -> List[int]:
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def binary_search(arr: List[int], target: int) -> (bool, int):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True, mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False, -1

def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left: List[int], right: List[int]) -> List[int]:
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def find_min(arr: List[int]) -> int:
    if not arr:
        raise ValueError("La lista está vacía")
    min_val = arr[0]
    for num in arr[1:]:
        if num < min_val:
            min_val = num
    return min_val


def calculate_mean_median(arr: List[int]) -> dict:
    if not arr:
        raise ValueError("La lista está vacía")
    n = len(arr)
    sorted_arr = bubble_sort(arr[:])
    mean = sum(arr) / n
    if n % 2 == 0:
        median = (sorted_arr[n // 2 - 1] + sorted_arr[n // 2]) / 2
    else:
        median = sorted_arr[n // 2]
    return {"mean": mean, "median": median}
