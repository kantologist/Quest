
def checkout_cart(cart_id, all, form):
    if all == False:
        if cart_id == None:
            raise ValueError("cart_id must be present")
        new_cart = update_session_cart(cart_id, **form.data)
        new_cart.cart_items=[]
        db.session.add(new_cart)
        db.session.commit()
        carts.carts.remove(new_cart)
        return redirect(url_for('main.index'))
    carts = fetchCart()
    for cart in carts.carts:
        new_cart = update_session_cart(cart.id, **form.data)
        new_cart.cart_items=[]
        db.session.add(new_cart)
        db.session.commit()
    carts.carts = []
    db.session.add(carts)
    db.session.commit()
    return redirect(url_for('main.index'))

@main.route('/checkout/<int:cart_id>')
@main.route('/checkout', methods=['GET','POST'])
def checkout(cart_id=None):
    carts = fetchCart()
    form = SessionCartForm()
    if request.method=='POST' and form.validate_on_submit():
        if not current_user.is_authenticated:
            return redirect(url_for('main.login'))
        cart_id = request.form.get('cart_id')
        checkout_cart(cart_id, all = (cart_id==None), form=form)
    return render_template('checkout.html', cart_id=cart_id, form=form, cart=carts)




if user_id:
            variant = Variant.query.filter_by(id=variant_id).first()
            cart = SessionCart.query.filter_by(user_id=user_id,
                                               shop_id=variant.product.shop_id).first()
            if not cart:
                cart_item = SessionCartItem.query.filter(SessionCartItem.variant_id == variant_id).first()
                cart = cart_item.session_cart
            cart.add_item(variant_id, quantity, replace=True, **kwargs)
            cart.aggregated_cart = self
            db.session.add(cart)
            db.session.commit()
            print("Item Successfully added to SessionCart")
            return None
        
