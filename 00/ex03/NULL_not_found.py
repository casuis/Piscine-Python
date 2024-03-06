def NULL_not_found(object: any) -> int:
	match(object):
		case None:
			print("Nothing:", end=" ")
		case _ if object != object:
			print("Cheese:", end=" ")
		case 0 if type(object) is int:
			print("Zero:", end=" ")
		case '' :
			print("Empty:", end="")
		case False: 
			print("Fake:", end=" ")
		case _:
			print("Type not Found")
			return 1
	print(object, type(object))
	return 0