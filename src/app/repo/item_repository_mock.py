from typing import Dict, Optional, List

from ..enums.item_type_enum import ItemTypeEnum
from ..entities.item import Item
from .item_repository_interface import IItemRepository


class ItemRepositoryMock(IItemRepository):
    items: Dict[int, Item]
    
    def __init__(self):
        self.items = {
          
        }
        
    def get_all_items(self) -> List[Item]:
        return self.items.values()
    
    def get_item(self, item_id: int) -> Optional[Item]:
        return self.items.get(item_id, None)
    
    def create_item(self, item: Item, item_id: int) -> Item:
        
        self.items[item_id] = item
        return item
    
    # Vamos criar um metodo para deletar o item, garantindo que ele exista e seja um booleano

    # Vamos criar um metodo para atualizar o item, garantindo que ele exista e seja um booleano
        
    
    