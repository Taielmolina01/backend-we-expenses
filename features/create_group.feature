Feature: Creación de grupos

Scenario: Crear un grupo sin nombre
	Given estoy registrado en la aplicación
	When creo un grupo sin nombre
	Then no se crea el grupo

Scenario: Crear un grupo con nombre
	Given estoy registrado en la aplicación
	When creo un grupo con nombre
	Then se crea el grupo

Scenario: Invitar amigos no registrados
  Given estoy registrado en la aplicación
  When invito a mi grupo a mis amigos por emails no registrados
  Then no los invito

Scenario: Invitar amigos registrados
  Given estoy registrado en la aplicación
  When invito a mi grupo a mis amigos por emails registrados
  Then los invito