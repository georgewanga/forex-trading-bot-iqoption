from iqoptionapi.stable_api import IQ_Option
import time


def login(username, password):
    iqoption = IQ_Option(username, password)
    check, reason = iqoption.connect()
    if check:
        print("Login successful!")
    else:
        print(f"Login failed: {reason}")
    return iqoption


def trade(iqoption, pair, amount, action):
    check, id = iqoption.buy(amount, pair, action)
    if check:
        print(f"Order placed: {action} {amount} on {pair}")
    else:
        print("Order failed!")


if __name__ == "__main__":
    iqoption = login("george.wanga@gmail.com", "27959256")

    trade(iqoption, "EURUSD", 10, "call")

    # Check trade result
    time.sleep(60)  # Simulate waiting for trade result
    result = iqoption.get_profit_after_sale("EURUSD")
    print(f"Trade result: {result}")
