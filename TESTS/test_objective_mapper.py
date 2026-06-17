from APP.Objectives.ObjectiveMapper import ObjectiveMapper


mapper = ObjectiveMapper()

print("\nOBJETIVOS DISPONIBLES\n")
print(mapper.list_objectives())

print("\nCRECER\n")
print(mapper.get_dimensions("crecer"))
print(mapper.get_agents("crecer"))

print("\nAUMENTAR RENTABILIDAD\n")
print(mapper.get_dimensions("aumentar_rentabilidad"))
print(mapper.get_agents("aumentar_rentabilidad"))