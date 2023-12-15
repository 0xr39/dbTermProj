# ERC-20 Dex Trades DB Example

## Activation Steps
### Activate
   ```shell
source env/bin/activate
```
### Deactivate
```
deactivate
```

## start server
```
uvicorn app.main:app --port 3000 --reload
```

## File Structure

```bash
   code
   ├── app
   │   ├── controllers
   │   │   └── user_controller.py
   │   ├── models
   │   │   └── user.py
   │   └── views
   │       └── user_view.py
   └── main.py
```

## endpoints

/create : create the db
/getholder/{tokenAddress} : retrive all holders of the token
