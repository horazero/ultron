import numpy_financial as npf
from scipy.optimize import newton

def pv(annual_rate, number_periods, payment, future_value, when=type):
    return npf.pv(annual_rate, number_periods, payment, future_value, when=when).round(3)


def rate(number_periods, payment, present_value, future_value=0, type=0, guess=0.1):
    # Define the rate equation to solve
    def rate_equation(r):
        if type == 1:
            output = present_value * (1 + r)**number_periods + payment * (1 - (1 + r)**-number_periods) / r * (1 + r) + future_value
        else:
            output = present_value * (1 + r)**number_periods + payment * (1 - (1 + r)**-number_periods) / r + future_value
        return output.round(3)
    return newton(rate_equation, guess)

def bond_ytm(price, face_value, coupon_rate, years, frequency=2):
    """
    Calculate the Yield to Maturity (YTM) for a bond.
    
    Parameters:
        price (float): The bond's current price
        face_value (float): The face value or redemption value of the bond
        coupon_rate (float): The annual coupon rate (e.g., 0.05 for 5%)
        years (int): The number of years until maturity
        frequency (int): Number of coupon payments per year (default is 2 for semi-annual)
        
    Returns:
        float: The annual yield to maturity (YTM)
    """
    
    # Calculate the coupon payment (annual coupon rate * face value) divided by frequency
    coupon_payment = coupon_rate * face_value / frequency
    
    # Define the YTM equation
    def ytm_equation(r):
        total_value = 0
        # Sum the present value of the coupon payments
        for t in range(1, years * frequency + 1):
            total_value += coupon_payment / (1 + r / frequency)**t
        # Add the present value of the face value
        total_value += face_value / (1 + r / frequency)**(years * frequency)
        return total_value - price
    
    # Use Newton's method to solve for the YTM
    ytm = newton(ytm_equation, 0.05)  # Initial guess for the YTM is 5%