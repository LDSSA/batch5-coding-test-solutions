import numpy as np


def test_exercise_2_I(read_products):
    
    
    products_data = read_products("products.csv")

    assert len(products_data) == 13
    
    assert "Iogurt" in products_data
    iogurt = products_data["Iogurt"]
    assert iogurt["idx"] == 3
    assert iogurt["category"] == "dairy"
    np.testing.assert_almost_equal(iogurt["price_kg"], 2.3, decimal=1)
    np.testing.assert_almost_equal(iogurt["kcal_kg"], 1300, decimal=1)
    assert isinstance(iogurt["price_kg"], float)
    assert isinstance(iogurt["kcal_kg"], float)
    
    assert "Chickpea" in products_data
    chickpea = products_data["Chickpea"]
    assert chickpea["idx"] == 9
    assert chickpea["category"] == "vegetable"
    np.testing.assert_almost_equal(chickpea["price_kg"], 1.2, decimal=1)
    np.testing.assert_almost_equal(chickpea["kcal_kg"], 3780, decimal=1)
    assert isinstance(chickpea["price_kg"], float)
    assert isinstance(chickpea["kcal_kg"], float)
    

def test_exercise_2_II(recipe_price_kcal):
    
    products_data = {
        "Flour": {"idx": 0, "category": "cereal", "price_kg": 0.5, "kcal_kg": 3500.0},
        "Sugar": {"idx": 1, "category": "other", "price_kg": 0.7, "kcal_kg": 4000.0},
        "Egg": {"idx": 2, "category": "protein", "price_kg": 6.5, "kcal_kg": 1320.0},
        "Sunflower oil": {"idx": 4, "category": "oil", "price_kg": 1.7, "kcal_kg": 8300.0},
        "Carrot": {"idx": 5, "category": "vegetable", "price_kg": 0.75, "kcal_kg": 450.0},
        "Avocado": {"idx": 6, "category": "fruit", "price_kg": 4.5, "kcal_kg": 1600.0},
        "Onion": {"idx": 7, "category": "vegetable", "price_kg": 1.0, "kcal_kg": 400.0},
        "Tomato": {"idx": 8, "category": "fruit", "price_kg": 1.8, "kcal_kg": 180.0},
        "Chickpea": {"idx": 9, "category": "vegetable", "price_kg": 1.2, "kcal_kg": 3780.0},
        "Tahini": {"idx": 10, "category": "paste", "price_kg": 11.3, "kcal_kg": 6200.0},
        "Olive oil": {"idx": 11, "category": "oil", "price_kg": 3.5, "kcal_kg": 8280.0},
        "Garlic": {"idx": 12,"category": "vegetable","price_kg": 3.6,"kcal_kg": 1490.0}
    }
    
    hummus_recipe = {
        "Chickpea": 0.5,
        "Tahini": 0.05,
        "Olive oil": 0.1,
        "Garlic": 0.02
    }
    
    guacamole_recipe = {
        "Avocado": 0.45,
        "Onion": 0.1,
        "Tomato": 0.15,
    }
    
    carrot_cake_recipe = {
        "Carrot": 0.35,
        "Egg": 0.2,
        "Flour": 0.25,
        "Sugar": 0.2,
        "Sunflower oil": 0.1
    }
    
    hummus_price_kcal = recipe_price_kcal(products_data, hummus_recipe)
    assert isinstance(hummus_price_kcal, tuple)
    assert len(hummus_price_kcal) == 2
    np.testing.assert_almost_equal(hummus_price_kcal[0], 1.59, decimal=2)
    np.testing.assert_almost_equal(hummus_price_kcal[1], 3057.8, decimal=2)
    
    guacamole_price_kcal = recipe_price_kcal(products_data, guacamole_recipe)
    assert isinstance(guacamole_price_kcal, tuple)
    assert len(guacamole_price_kcal) == 2
    np.testing.assert_almost_equal(guacamole_price_kcal[0], 2.40, decimal=2)
    np.testing.assert_almost_equal(guacamole_price_kcal[1], 787.0, decimal=2)
    
    carrot_cake_price_kcal = recipe_price_kcal(products_data, carrot_cake_recipe)
    assert isinstance(carrot_cake_price_kcal, tuple)
    assert len(carrot_cake_price_kcal) == 2
    np.testing.assert_almost_equal(carrot_cake_price_kcal[0], 2.00, decimal=2)
    np.testing.assert_almost_equal(carrot_cake_price_kcal[1], 2926.5, decimal=2)


def test_exercise_3_II(track_passengers, Bus):
    bus = Bus(1, [1, 2, 3], 10)
    
    stops = [
        {"enter": 10, "leave": 0},
        {"enter": 2, "leave": 0},
        {"enter": 2, "leave": 1},
        {"enter": 0, "leave": 10},
    ]

    passengers = track_passengers(bus, stops)

    assert isinstance(passengers, list)
    assert len(passengers) == 4
    assert passengers == [10, 10, 10, 0]
    
    bus = Bus(1, [1, 2, 3], 50)
    
    stops = [
        {"enter": 10, "leave": 0},
        {"enter": 10, "leave": 0},
        {"enter": 10, "leave": 0},
        {"enter": 10, "leave": 0},
        {"enter": 10, "leave": 0},
        {"enter": 5, "leave": 10},
    ]

    passengers = track_passengers(bus, stops)

    assert isinstance(passengers, list)
    assert len(passengers) == 6
    assert passengers == [10, 20, 30, 40, 50, 45]
    

def test_exercise_4_I(get_adjacent_cells):
    tests = [
        {
            "cell_position": (0, 2),
            "mines_map_shape": (1, 3),
            "expected_answer": [(0, 1)],
        },
        {
            "cell_position": (9, 1),
            "mines_map_shape": (10, 3),
            "expected_answer": [(8, 0), (8, 1), (8, 2), (9, 0), (9, 2)],
        },
    ]

    for test in tests:
        answer = get_adjacent_cells(test["cell_position"], test["mines_map_shape"])
        
        assert isinstance(answer, list)
        assert set(answer) == set(test["expected_answer"])
        for position in answer:
            assert isinstance(position, tuple)

    
def test_exercise_4_II(get_clues_map):
    mines_map = np.array([
        ["-", "*"],
        ["-", "-"],
    ])

    clues_map = get_clues_map(mines_map)

    assert isinstance(clues_map, np.ndarray)
    assert clues_map.shape == mines_map.shape
    np.testing.assert_array_equal(
        clues_map, 
        np.array([
            [ 1, -1],
            [ 1,  1],
        ])
    )
    
    mines_map = np.array([
        ["-", "*", "-", "-"],
        ["-", "*", "-", "-"],
        ["-", "*", "*", "*"],
    ])

    clues_map = get_clues_map(mines_map)

    assert isinstance(clues_map, np.ndarray)
    assert clues_map.shape == mines_map.shape
    np.testing.assert_array_equal(
        clues_map, 
        np.array([
            [ 2, -1,  2,  0],
            [ 3, -1,  5,  2],
            [ 2, -1, -1, -1],
        ])
    )
    
def test_exercise_4_III(get_number_mines):
    clues_map = np.array([
        [ 1, -1],
        [ 1,  1],
    ])
    
    num_mines = get_number_mines(clues_map)
    assert num_mines == 1
    
    clues_map = np.array([
        [ 2, -1,  2,  0],
        [ 3, -1,  5,  2],
        [ 2, -1, -1, -1],
    ])
    
    num_mines = get_number_mines(clues_map)
    assert num_mines == 5