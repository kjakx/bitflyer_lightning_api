from apihitter import ApiHitter

class PrivateAPI(ApiHitter):
    def __init__(self, key, secret):
        super().__init__(key, secret)

    def getPermissions(self):
        return self.request("GET", "/v1/me/getpermissions")
        
    def getBalance(self):
        return self.request("GET", "/v1/me/getbalance")

    def getCollateral(self):
        return self.request("GET", "/v1/me/getcollateral")

    def getCollateralAccounts(self):
        return self.request("GET", "/v1/me/getcollateralaccounts")

    def sendChildOrder( self, \
                        product_code, \
                        child_order_type, side, price=None, size=0.01, \
                        minute_to_expire=43200, \
                        time_in_force="GTC"):
        return self.request("POST", "/v1/me/sendchildorder", \
                            product_code=product_code, \
                            child_order_type=child_order_type, \
                            side=side, price=price, size=size, \
                            minute_to_expire=minute_to_expire, \
                            time_in_force=time_in_force)

    def sendParentOrder(self, \
                        order_method="SIMPLE", \
                        minute_to_expire=43200, \
                        time_in_force="GTC", \
                        parameters=[]):
        return self.request("POST", "/v1/me/sendparentorder", \
                            order_method="SIMPLE", \
                            minute_to_expire=minute_to_expire, \
                            time_in_force=time_in_force, \
                            parameters=parameters)

    def cancelChildOrder(   self, \
                            product_code, \
                            child_order_id=None, \
                            child_order_acceptance_id=None):
        return self.request("POST", "/v1/me/cancelchildorder", \
                            product_code=product_code, \
                            child_order_id=child_order_id, \
                            child_order_acceptance_id=child_order_acceptance_id)

    def cancelParentOrder(  self, \
                            product_code, \
                            parent_order_id=None, \
                            parent_order_acceptance_id=None):
        return self.request("POST", "/v1/me/cancelparentorder", \
                            product_code=product_code, \
                            parent_order_id=parent_order_id, \
                            parent_order_acceptance_id=parent_order_acceptance_id)

    def cancelAllChildOrders(self, product_code):
        return self.request("POST", "/v1/me/cancelallchildorders", \
                            product_code=product_code)

    def getChildOrders( self, \
                        product_code, count=100, before=0, after=0, \
                        child_order_state=None, \
                        child_order_id=None, \
                        child_order_acceptance_id=None, \
                        parent_order_id=None ):
        return self.request("GET", "/v1/me/getchildorders", \
                            product_code=product_code, \
                            count=count, before=before, after=after, \
                            child_order_state=child_order_state, \
                            child_order_id=child_order_id, \
                            child_order_acceptance_id=child_order_acceptance_id, \
                            parent_order_id=parent_order_id)

    def getParentOrders(self, \
                        product_code, count=100, before=0, after=0, \
                        parent_order_state=None):
        return self.request("GET", "/v1/me/getparentorders", \
                            product_code=product_code, \
                            count=count, before=before, after=after, \
                            parent_order_state=parent_order_state)
    
    def getParentOrder( self, \
                        parent_order_id=None, parent_order_acceptance_id=None):
        return self.request("GET", "/v1/me/getparentorder", \
                            parent_order_id=parent_order_id, \
                            parent_order_acceptance_id=parent_order_acceptance_id)

    def getMyExecutions(self, \
                        product_code, count=100, before=0, after=0, \
                        child_order_id=None, \
                        child_order_acceptance_id=None):
        return self.request("GET", "/v1/me/getexecutions", \
                            product_code=product_code, \
                            count=count, before=before, after=after, \
                            child_order_id=child_order_id, \
                            child_order_acceptance_id=child_order_acceptance_id)

    def getPositions(self, product_code):
        return self.request("GET", "/v1/me/getpositions", product_code=product_code)

    def getCollateralHistory(self, count=100, before=0, after=0):
        return self.request( "GET", "/v1/me/getcollateralhistory", \
                            count=count, before=before, after=after)

    def getTradingCommission(self, product_code):
        return self.request("GET", "/v1/me/getpositions", product_code=product_code)

    def getAddresses(self):
        return self.request("GET", "/v1/me/getaddresses")

    def getCoinIns(self, count=100, before=0, after=0):
        return self.request("GET", "/v1/me/getcoinins", \
                            count=count, before=before, after=after )

    def getCoinOuts(self, count=100, before=0, after=0, message_id=None):
        return self.request("GET", "/v1/me/getcoinouts", \
                            count=count, before=before, after=after, \
                            message_id=message_id)

    def getDeposits(self, count=100, before=0, after=0):
        return self.request("GET", "/v1/me/getdeposits", \
                            count=count, before=before, after=after )

    def getWithdrawals(self, count=100, before=0, after=0, message_id=None):
        return self.request("GET", "/v1/me/getwithdrawals", \
                            count=count, before=before, after=after, \
                            message_id=message_id )

    def getBankAccounts(self):
        return self.request("GET", "/v1/me/getbankaccounts")

    def withdraw(self, currency_code, bank_account_id, amount, code):
        return self.request("POST", "/v1/me/withdraw", currency_code=currency_code, \
                            bank_account_id=bank_account_id, amount=amount, code=code)

if __name__ == "__main__":
    api = PrivateAPI( \
        key = "YOUR_API_KEY", \
        secret = "YOUR_API_SECRET")
    print(api.getBalance())
    """
    print(api.sendChildOrder(\
                        product_code="FX_BTC_JPY", \
                        child_order_type="LIMIT", \
                        price=114514, \
                        side="BUY", \
                        size=0.01))
    """