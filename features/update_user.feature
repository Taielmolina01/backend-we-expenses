Feature: Registro de usuario

Scenario: Actualizo un usuario inexistente
  Given no estoy registrado
  When actualizo mi perfil
  Then se me indica que no existe el usuario

Scenario: Actualizo un usuario existente con datos inválidos
  Given estoy registrado
  When actualizo mi perfil con datos inválidos
  Then no se actualiza
  
Scenario: Actualizo un usuario exitente con datos válidos
  Given estoy registrado
  When actualizo mi perfil con datos válidos
  Then se actualiza