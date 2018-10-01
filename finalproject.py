from flask import Flask
app = Flask(__name__)

# Rotas para a aplicacao
@app.route('/')
@app.route('/restaurants/')
def showRestaurants():
    return 'this page will show all my restaurants'

@app.route('/restaurant/new/')
def newRestaurant():
    return 'this page will be for making a new restaurant'

@app.route('/restaurant/<int:restaurant_id>/edit/')
def editRestaurant():
    return 'this page will be for editing restaurants'

@app.route('/restaurant/<int:restaurant_id>/delete/')
def deleteRestaurant():
    return 'this page will be for deleting restaurants'

@app.route('/restaurant/<int:restaurant_id>/')
@app.route('/restaurant/<int:restaurant_id>/menu/')
def showMenu(restaurant_id):
    return 'this page will be for the menu'

@app.route('/restaurant/<int:restaurant_id>/menu/new/')
def newMenuItem(restaurant_id):
    return 'this page is to create new menu items'

@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/edit/')
def editMenuItem(restaurant_id, menu_id):
    return 'this page is to edit menu items'

@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/delete/')
def deleteMenuItem(restaurant_id, menu_id):
    return 'this page is to delete menu items'


#====================!!!!=======================

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
