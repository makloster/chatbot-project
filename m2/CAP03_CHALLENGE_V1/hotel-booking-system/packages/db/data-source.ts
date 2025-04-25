import { DataSource } from "typeorm";

export const AppDataSource = new DataSource({
  type: "postgres",
  host: "localhost",
  port: 5432,
  username: "postgres",
  password: "postgres",
  database: "hotel_booking",
  entities: [__dirname + "/../api/**/entities/*.entity{.ts,.js}"],
  synchronize: true,
});
