#!/usr/bin/env python3
"""
Initialize the FoodForge database with schema and default data.
Run this script to create the database and populate fridge locations.
"""

from database import init_db, get_session
from models import FridgeLocation, User

def populate_fridge_locations():
    """Populate the fridge_locations table with default locations based on the schema diagram."""
    session = get_session()
    
    # Check if locations already exist
    existing_count = session.query(FridgeLocation).count()
    if existing_count > 0:
        print(f"Fridge locations already exist ({existing_count} locations). Skipping...")
        return
    
    # Define fridge locations based on the schema diagram
    locations = [
        # Main Refrigerator - Top Section
        FridgeLocation(name='Top Shelf', section='Top', temperature='Cold'),
        FridgeLocation(name='Mid Shelf', section='Top', temperature='Cold'),
        FridgeLocation(name='Bottom Shelf', section='Top', temperature='Cold'),
        FridgeLocation(name='Vegetable Crisper', section='Top', temperature='Cold'),
        FridgeLocation(name='Fruit Crisper', section='Top', temperature='Cold'),
        FridgeLocation(name='Meat Storage', section='Top', temperature='Cold'),
        
        # Freezer Section
        FridgeLocation(name='Bottom Basket', section='Freezer', temperature='Frozen'),
        FridgeLocation(name='Bottom Basket (Left)', section='Freezer', temperature='Frozen'),
        FridgeLocation(name='Bottom Basket (Right)', section='Freezer', temperature='Frozen'),
        FridgeLocation(name='Roller Shelf', section='Freezer', temperature='Frozen'),
        
        # Left Door
        FridgeLocation(name='Left Door - Top Shelf', section='Left Door', temperature='Cold'),
        FridgeLocation(name='Left Door - Mid Shelf', section='Left Door', temperature='Cold'),
        FridgeLocation(name='Left Door - Bottom Shelf', section='Left Door', temperature='Cold'),
        
        # Right Door
        FridgeLocation(name='Right Door - Top Shelf', section='Right Door', temperature='Cold'),
        FridgeLocation(name='Right Door - Mid Shelf', section='Right Door', temperature='Cold'),
        FridgeLocation(name='Right Door - Bottom Shelf', section='Right Door', temperature='Cold'),
    ]
    
    # Add all locations to the session
    for location in locations:
        session.add(location)
    
    # Commit the changes
    session.commit()
    print(f"Successfully added {len(locations)} fridge locations!")
    
    # Display the locations
    print("\nFridge Locations:")
    for loc in locations:
        print(f"  - {loc.name} ({loc.section}, {loc.temperature})")
    
    session.close()

def create_default_user():
    """Create a default user for testing."""
    session = get_session()
    
    # Check if user already exists
    existing_user = session.query(User).filter_by(username='default').first()
    if existing_user:
        print("Default user already exists. Skipping...")
        return
    
    # Create default user
    user = User(username='default', email='user@foodforge.local')
    session.add(user)
    session.commit()
    print(f"Created default user: {user.username} (ID: {user.id})")
    session.close()

if __name__ == '__main__':
    print("Initializing FoodForge Database...")
    print("=" * 50)
    
    # Create all tables
    init_db()
    
    # Populate with default data
    print("\nPopulating fridge locations...")
    populate_fridge_locations()
    
    print("\nCreating default user...")
    create_default_user()
    
    print("\n" + "=" * 50)
    print("Database initialization complete!")
    print("Database file: foodforge.db")
