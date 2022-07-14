**Welcome** to the ***RestFramework***  `API`  
=

**`Authentication`**
-
~~~
http://localhost:8000/api/auth/
~~~
This end point will take you to the authentication. You need to pass credencials here for example:
~~~
{
    "first_name" : "Your name",
    "last_name" : "last name",
    "email" : "example@test.com",
    "username" : "test123",
    "password" : " Secret ***** ",

}
~~~

It will return you in response **`Authentication Token`**, with the token u can authentication your self with the given **`Token`** .
#
**`Adding the Stock DATA `**
-
~~~
http://localhost:8000/api/add-stock/
~~~

You have to pass the data in the given format to save successfully . `Get the format below`
~~~ 
{

    "stock_name" : "aple", 
    "stock_quantity" : 56, 
    "date" : "1998-08-23", 
    "purchased_price" : 456

}

*Note : Date format ( YYYY-MM-DD )

~~~

To perform this action u need to stay loged in or so pass the `Authentication Token` with the request. 
**Note: Please check the stock name twice add `Full name` of the stock*
#

**`Fetching the DATA `**
-
~~~
http://localhost:8000/api/all/
~~~
You wil get your all of your saved stock data.