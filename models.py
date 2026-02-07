from sqlalchemy import Column, Integer, String, DateTime, Numeric, Boolean, Date, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    receipts = relationship('Receipt', back_populates='user', cascade='all, delete-orphan')
    recipes = relationship('Recipe', back_populates='user', cascade='all, delete-orphan')
    fridge_items = relationship('FridgeItem', back_populates='user', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}')>"


class Receipt(Base):
    __tablename__ = 'receipts'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    file_path = Column(String(255), nullable=False)
    upload_date = Column(DateTime, default=datetime.utcnow)
    store_name = Column(String(100))
    purchase_date = Column(Date)
    total_amount = Column(Numeric(10, 2))
    processed = Column(Boolean, default=False)
    
    # Relationships
    user = relationship('User', back_populates='receipts')
    items = relationship('ReceiptItem', back_populates='receipt', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f"<Receipt(id={self.id}, store='{self.store_name}', date={self.purchase_date})>"


class ReceiptItem(Base):
    __tablename__ = 'receipt_items'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    receipt_id = Column(Integer, ForeignKey('receipts.id'), nullable=False)
    item_name = Column(String(200), nullable=False)
    quantity = Column(Numeric(10, 2))
    unit = Column(String(20))
    price = Column(Numeric(10, 2))
    category = Column(String(50))
    
    # Relationships
    receipt = relationship('Receipt', back_populates='items')
    
    def __repr__(self):
        return f"<ReceiptItem(id={self.id}, name='{self.item_name}', qty={self.quantity})>"


class Recipe(Base):
    __tablename__ = 'recipes'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    title = Column(String(200), nullable=False)
    source_file = Column(String(255))
    upload_date = Column(DateTime, default=datetime.utcnow)
    prep_time = Column(Integer)  # in minutes
    cook_time = Column(Integer)  # in minutes
    servings = Column(Integer)
    instructions = Column(Text)
    
    # Relationships
    user = relationship('User', back_populates='recipes')
    recipe_ingredients = relationship('RecipeIngredient', back_populates='recipe', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f"<Recipe(id={self.id}, title='{self.title}')>"


class Ingredient(Base):
    __tablename__ = 'ingredients'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), unique=True, nullable=False)
    category = Column(String(50))
    
    # Relationships
    recipe_ingredients = relationship('RecipeIngredient', back_populates='ingredient')
    
    def __repr__(self):
        return f"<Ingredient(id={self.id}, name='{self.name}')>"


class RecipeIngredient(Base):
    __tablename__ = 'recipe_ingredients'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    recipe_id = Column(Integer, ForeignKey('recipes.id'), nullable=False)
    ingredient_id = Column(Integer, ForeignKey('ingredients.id'), nullable=False)
    quantity = Column(Numeric(10, 2))
    unit = Column(String(20))
    notes = Column(String(200))
    
    # Relationships
    recipe = relationship('Recipe', back_populates='recipe_ingredients')
    ingredient = relationship('Ingredient', back_populates='recipe_ingredients')
    
    def __repr__(self):
        return f"<RecipeIngredient(recipe_id={self.recipe_id}, ingredient_id={self.ingredient_id})>"


class FridgeLocation(Base):
    __tablename__ = 'fridge_locations'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    section = Column(String(50))  # e.g., "Main", "Freezer", "Left Door", "Right Door"
    temperature = Column(String(20))  # e.g., "Cold", "Frozen"
    
    # Relationships
    fridge_items = relationship('FridgeItem', back_populates='location')
    
    def __repr__(self):
        return f"<FridgeLocation(id={self.id}, name='{self.name}', section='{self.section}')>"


class FridgeItem(Base):
    __tablename__ = 'fridge_items'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    item_name = Column(String(200), nullable=False)
    location_id = Column(Integer, ForeignKey('fridge_locations.id'), nullable=False)
    quantity = Column(Numeric(10, 2))
    unit = Column(String(20))
    added_date = Column(DateTime, default=datetime.utcnow)
    expiry_date = Column(Date)
    category = Column(String(50))
    image_path = Column(String(255))
    
    # Relationships
    user = relationship('User', back_populates='fridge_items')
    location = relationship('FridgeLocation', back_populates='fridge_items')
    removals = relationship('ItemRemoval', back_populates='fridge_item', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f"<FridgeItem(id={self.id}, name='{self.item_name}', location_id={self.location_id})>"


class ItemRemoval(Base):
    __tablename__ = 'item_removals'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    fridge_item_id = Column(Integer, ForeignKey('fridge_items.id'), nullable=False)
    removed_date = Column(DateTime, default=datetime.utcnow)
    quantity = Column(Numeric(10, 2))
    verification_image = Column(String(255))
    verified = Column(Boolean, default=False)
    
    # Relationships
    fridge_item = relationship('FridgeItem', back_populates='removals')
    
    def __repr__(self):
        return f"<ItemRemoval(id={self.id}, fridge_item_id={self.fridge_item_id}, qty={self.quantity})>"
