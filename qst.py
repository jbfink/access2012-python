def gst(price):
	return price * 0.05

def qst(price):
	return (price + gst(price)) * 0.085

def total(price):
	return gst(price) + qst(price) + price


