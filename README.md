# Website for my dear friend  
___
To migrate:  
```
cd ..  
cd backend  
alembic revision --autogenerate -m "Your migration message"  
alembic upgrade head  
```