from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel
from passlib.context import CryptContext
import jwt

fake_db = {"users": {}}

app = FastAPI()

class Payload(BaseModel):
    numbers: List[int]

class BinarySearchPayload(BaseModel):
    numbers: List[int]
    target: int

# 1️⃣ Algoritmo Bubble Sort
def bubble_sort(arr: List[int]) -> List[int]:
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

@app.post("/bubble-sort")
async def bubble_sort_endpoint(payload: Payload):
    sorted_numbers = bubble_sort(payload.numbers)
    return {"numbers": sorted_numbers}

# 2️⃣ Filtro de Pares
@app.post("/filter-even")
async def filter_even_numbers(payload: Payload):
    even_numbers = [num for num in payload.numbers if num % 2 == 0]
    return {"even_numbers": even_numbers}

# 3️⃣ Suma de Elementos
@app.post("/sum-elements")
async def sum_elements(payload: Payload):
    total_sum = sum(payload.numbers)
    return {"sum": total_sum}

# 4️⃣ Máximo Valor
@app.post("/max-value")
async def max_value(payload: Payload):
    if not payload.numbers:
        raise HTTPException(status_code=400, detail="La lista de números no puede estar vacía.")
    max_number = max(payload.numbers)
    return {"max": max_number}

# 5️⃣ Búsqueda Binaria
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

@app.post("/binary-search")
async def binary_search_endpoint(payload: BinarySearchPayload):
    sorted_numbers = bubble_sort(payload.numbers)  # Asegurar que la lista esté ordenada
    found, index = binary_search(sorted_numbers, payload.target)
    return {"found": found, "index": index}
