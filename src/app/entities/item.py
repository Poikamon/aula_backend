from typing import Tuple
from ..errors.entity_errors import ParamNotValidated
from ..enums.item_type_enum import ItemTypeEnum
import re

class user:
    name: str
    agency: str
    account: str
    account_balance: float
    
    def __init__(self, name: str=None,  agency: str=None, account: str=None, account_balance: float=None):
        validation_name = self.validate_name(name)
        if validation_name[0] is False:
            raise ParamNotValidated("name", validation_name[1])
        self.name = name
        
       
        validation_agency = self.validate_agency(agency)
        if validation_agency[0] is False:
            raise ParamNotValidated("agency", validation_agency[1])
        self.agency = agency
        

        validation_account = self.validate_account(account)
        if validation_account[0] is False:
            raise ParamNotValidated("account", validation_account[1])
        self.account = account

        validation_account_balance = self.validate_account_balance(account_balance)
        if validation_account_balance[0] is False:
            raise ParamNotValidated("account_balance", validation_account_balance[1])
        self.account_balance = account_balance


#@staticmethod ? 
#as funções validate recebem info como "def validate_name'(name: str), usado para vc se guiar no código, logo n muito ncessário' -> Tuple [bool, str] 
#(tuples são charac. imutáveis de um objt. e nesse caso define que retorna uma booleana com primeiro elemento e str como segunda)	if name is None: 
#return (false, "name is required")"
    @staticmethod
    def validate_name(name: str) -> Tuple[bool, str]:
        if name is None:
            return (False, "O nome?! Cadê!?")
        if type(name) != str:
            return (False, "String doidão/doidona, string.")
        if len(name) == 0: 
            return (False, "Ué!? Cadê!? :(")
        return (True, "")

    @staticmethod
    def validate_agency(agency: str) -> Tuple[bool, str]:
        if agency is None:
            return (False, "E a agencia!? Cadê!?")
        if type(agency) != str:
            return (False, "Tem que ser string, meu/minha cumpade.")
        if len(agency) == 4:
            return (False, "Tem que ser 4 numeros, siga o formato maninho/a.")
        return (True, "")
    
    @staticmethod
    def validate_account(account: str) -> Tuple[bool, str]:
        if account is None:
            return (False, "E a conta!? Cadê!?")
        if not isinstance(account, str):
            return (False, "Ei, string né?")
        if not re.fullmatch(r"\d{5}-\d", account):
             return (False, "Não, não. Use o padrão XXXXX-X.")
        return (True, "")
        
    
    @staticmethod
    def validate_account_balance(account_balance: float) -> Tuple[bool, str]:
        if account_balance is None:
            return (False, "Eae, cadê o saldo? nada!?")
        if type(account_balance) != float:
            return (False, "Parameter 'item_id' must be an integer")
        if account_balance < 0:
            return (False, "Não tem como ter saldo negativo, né?")
        return (True, "")
    
        
    def to_dict(self): 
        return {
            "name": self.name,
            "agency": self.agency,
            "account": self.account,
            "account_balance": self.account_balance
        }
    
    def __eq__(self,other):
        return self.name == other.name and self.agency == other.agency and self.account == other.account and self.account_balance == other.account_balance
    
    def __repr__(self):
        return f"Item(name={self.name}, agency={self.agency}, account={self.account}, account_balance={self.account_balance})"