"""Queries to answer following questions"""

# How many total Characters are there?
QUERY_1 = '''SELECT COUNT(*)
            FROM charactercreator_character;'''

# How many of each specific subclass?
QUERY_2 = '''SELECT (
		SELECT COUNT(*)
		FROM charactercreator_thief
		) AS thief_class,
		(
		SELECT COUNT(*)
		FROM charactercreator_cleric
		) AS cleric_class,
		(
		SELECT COUNT(*)
		FROM charactercreator_fighter
		) AS fighter_class,
		(
		SELECT COUNT(*)
		FROM charactercreator_mage
		LEFT JOIN charactercreator_necromancer
		ON character_ptr_id = mage_ptr_id
		WHERE mage_ptr_id IS NOT NULL
		) AS Necromancer_class,
		(SELECT COUNT(*)
		FROM charactercreator_mage
		LEFT JOIN charactercreator_necromancer
		ON character_ptr_id = mage_ptr_id
		WHERE mage_ptr_id IS NULL
		) AS Mage_class'''

# How many total items?
QUERY_3 = '''SELECT COUNT(*)
            FROM armory_item;'''

# How many of the items are weapons? How many are not?
QUERY_4 = '''SELECT COUNT(*)
            FROM armory_weapon'''

QUERY_5 = '''SELECT COUNT(*)
            FROM armory_item
            LEFT JOIN armory_weapon
            on item_id = item_ptr_id
            WHERE item_ptr_id IS NULL;'''

# How many items does each character have? (return first 20 rows)

# How many weapons does each character have? (return first 20 rows)

# On average, how many items does each character have?

# On average, how many weapons does each character have?