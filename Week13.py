products={123:"hammer", 846:"Wrench",982:"paintbrush"}

prod_id=int(input("Enter product id"))

print(products.pop(prod_id, str(prod_id)+"Not Found"))