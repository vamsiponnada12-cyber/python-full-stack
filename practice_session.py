
'''
#price = 5000 #check the type(price)
#accessing input from the user
price = int(input('Enter a price: '))
#discount_= 0.1 #type(discount)
disc_= float(input('Entre the discount in betweeen 0.1 and 0.2: '))
gst = 0.18
final_price = price - (price*disc_)
final_price = final_price + (final_price*gst)
print(f'Final price is: {final_price} ')

#operators --> Arithmetic,Assignment,Comparision,Membership,Logical,Isentity,Bitwise

#Assignment --> = (assigns),+= (update the value)

price = 2000

price += 500
print(price)

#comparision --> = compare the values <, >, <=, >=, ==, !=

#membership --> in, not in --> its checks for the value in a collection

#we will have diff price -> diff discount ->gst same
'''

prices = [15000,200,13000,25000,35000]

final_prices = []
#price <= 15000 then discount is 10%
#price >5000 --> to apply a discount
#price >20000 --> 15%
#get the final price in a list
for price in prices:
    if price<=15000 and price>5000:
     price = price-(price*0.1)
     final_prices.append(int(price))
     
    elif price>20000:
        price = price-(price*0.15)
        final_prices.append(int(price))
     
    elif price < 5000:
        final_prices.append(int(price))
print(final_prices)

        
        
        

























