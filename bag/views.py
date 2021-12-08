from django.shortcuts import render, redirect


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

# submit the form to this view including the product id and the quantity
def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    # get the quantity from the form
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    # get the bag variable if it exists in the session, or create it if it doesn't (an object)
    bag = request.session.get('bag', {})

    # if it exists update the quantity, otherwise add item to the bag
    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity
    
    request.session['bag'] = bag
    # print it to make sure
    print(request.session['bag'])
    return redirect(redirect_url)