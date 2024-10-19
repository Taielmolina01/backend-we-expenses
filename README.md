# backend-we-expenses

## TO DO

- [ ] Deberia tener un estado la deuda? creeria que si

- [ ] Payment 
    - [ ] Controller
        - [ ] Manejar errores

- [ ] Test

- [ ] Autenticación con JWT, la contraseña en DB debe ir hasheada
- [ ] Cuando hago una transacción le descuento lo que tiene que pagar cada uno al resto de usuarios del grupo != del que hizo la transacción. Al que hizo la transacción le sumo el valor de la transacción.
- [ ] Cuando elimino una transacción le "devuelvo" lo que debía pagar cada uno al resto de usuarios del grupo != del que hizo la transacción. Al que hizo la transacción le resto el valor de la transacción.

## RUN

Tenes que tener el .venv activado  con

`source .venv/bin/activate` 

recien ahi instalas dependencias con

`pip install -r requirements.txt`

y ahi corres

`uvicorn main:app --reload`
