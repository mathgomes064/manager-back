import { DataSource } from "typeorm";


export const AppDataSource = new DataSource({
    type: "postgres",
    
    url: process.env.DATABASE_URL,

    synchronize: false,
    logging: false,
    entities: [
        "src/entities/**/*.ts"
    ],
    migrations: [
        "src/migrations/**/*.ts"
    ]
})