import pytest
from src.app.entities.item import user
from src.app.enums.item_type_enum import ItemTypeEnum
from src.app.errors.entity_errors import ParamNotValidated


class Test_user:
    def test_user(self):
        user = user("Vitor Soller", '0000', '00000-0', 1000.0)
        assert user.name == "Vitor Soller"
        assert user.agency == '0000'
        assert user.account == '00000-0'
        assert user.account_balance == 1000.0


        
    def test_user_dict(self):
        user = user("Vitor Soller", '0000', '00000-0', 1000.0)
        assert user.to_dict() == {'name': 'Vitor Soller', 'agency': '0000', 'account': '00000-0', 'account_balance': 1000.0}
    
    def test_user_name_is_none(self):
        with pytest.raises(ParamNotValidated):
            user(agency='0000', account='00000-0', account_balance='1000.0')
            
    def test_user_name_is_not_string(self):
        with pytest.raises(ParamNotValidated):
            user(name=1, agency='0000', account='00000-0', account_balance=1000.0)
            
    def test_user_name_no_name_at_all_poggers(self):
        with pytest.raises(ParamNotValidated):
          user(name="" ,agency='0000', account='00000-0', account_balance=1000.0)        
     
    def test_user_agency_is_none(self):
        with pytest.raises(ParamNotValidated):
            user(name="Vitor Soller", account='00000-0', account_balance=1000.0)
            
    def test_user_agency_is_not_float(self):
        with pytest.raises(ParamNotValidated):
             user(name="Vitor Soller", agency="Bem-aventurados aqueles que lavam as suas vestiduras [no sangue do Cordeiro], para que lhes assista o direito à árvore da vida, e entrem na cidade pelas portas.", account='00000-0', account_balance=1000.0)

    def test_user_agency_isnt_4(self):
        with pytest.raises(ParamNotValidated):
            user(name="Vitor Soller", agency='000', account='00000-0', account_balance=1000.0)

    def test_user_account_is_none(self):
        with pytest.raises(ParamNotValidated):
            user(name="Vitor Soller", agency='0000', account_balance=1000.0)
        
    def test_user_account_is_not_str(self):
        with pytest.raises(ParamNotValidated):
            user(name="Vitor Soller", agency='0000', account=1, account_balance=1000.0)
    
    def test_user_account_not_the_pattern(self):
        with pytest.raises(ParamNotValidated):
            user(name="Vitor Soller", agency='0000', account='000000', account_balance=1000.0)

    def test_user_account_balance_is_none(self):
        with pytest.raises(ParamNotValidated):
            user(name="Vitor Soller", agency='0000', account=00000-0)

    def test_user_account_balance_is_not_float(self):
        with pytest.raises(ParamNotValidated):
            user(name="Vitor Soller", agency='0000', account='00000-0', account_balance="Bem-aventurados aqueles que lavam as suas vestiduras [no sangue do Cordeiro], para que lhes assista o direito à árvore da vida, e entrem na cidade pelas portas.")

    def test_user_account_balance_is_not_positive(self):
        with pytest.raises(ParamNotValidated):
            user(name="Vitor Soller", agency='0000', account='00000-0', account_balance=-1000.0)
  