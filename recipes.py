print( "Recipe Program" )

# Ingredients stored in variables
flour = 2               # cups
bakingSoda = 0.5        # tsp
salt = 0.5              # tsp
butter = 0.75           # cups
sugar = 0.5             # cups
eggs = 1                # egg
chocolateChips = 2      # cups

print( "" )
print( "Chocolate Chip Cookie Recipe" )
print( "" )
print( flour, "\t cups of Flour" )
print( bakingSoda, "\t tsps of Baking Soda" )
print( salt, "\t tsps of Salt" )
print( butter, "\t cups of Butter")
print( sugar, "\t cups of Sugar" )
print( eggs, " \t Eggs" )
print( chocolateChips, "\t cups of Chocolate Chips" )

print( "" )
batchQuantity = float( input( "How many batches would you like to make? (0.5 for half, 2 for double): " ) )

flour = 2 * batchQuantity
bakingSoda = 0.5 * batchQuantity       
salt = 0.5 * batchQuantity
butter = 0.75 * batchQuantity          
sugar = 0.5 * batchQuantity          
eggs = 1 * batchQuantity
chocolateChips = 2 * batchQuantity   


print( "" )
print( "Chocolate Chip Cookie Recipe", batchQuantity, "batches" )
print( "" )
print( flour, "\t cups of Flour" )
print( bakingSoda, "\t tsps of Baking Soda" )
print( salt, "\t tsps of Salt" )
print( butter, "\t cups of Butter")
print( sugar, "\t cups of Sugar" )
print( eggs, " \t Eggs" )
print( chocolateChips, "\t cups of Chocolate Chips" )

