from dash.testing.composite import DashComposite
from app import app

# Test 1: Verify the Header is present
def test_header_exists(dash_duo):
    dash_duo.start_server(app)
    # Search for the H1 element
    header = dash_duo.find_element("h1")
    assert header.text == "Pink Morsel Sales Visualiser"
    assert header.is_displayed()

# Test 2: Verify the Visualisation (Graph) is present
def test_visualization_exists(dash_duo):
    dash_duo.start_server(app)
    # Search for the graph by the ID we gave it in app.py
    graph = dash_duo.find_element("#sales-graph")
    assert graph.is_displayed()

# Test 3: Verify the Region Picker (Radio Items) is present
def test_region_picker_exists(dash_duo):
    dash_duo.start_server(app)
    # Search for the radio items by the ID we gave it in app.py
    picker = dash_duo.find_element("#region-filter")
    assert picker.is_displayed()