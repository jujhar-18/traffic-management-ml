from pymmi.mmi import MapMyIndia

# Initialize MapMyIndiaAPI object
mmi = MapMyIndia('0fab15e8c8f6ba878ae9e962cff23d15')

def search_place(start, end):
    """
    Perform a basic search for a place using MapMyIndiaAPI.
    
    Args:
    - query (str): The search query for the place.
    
    Returns:
    - results (list): List of search results.
    """
    # Perform search
    results = mmi.routing(start, end)
    
    return results

if __name__ == "__main__":
    # Example search query
    start = "Vivekananda Institute of Professional Studies"
    end = "South Extension Part 2"

    # Perform search
    search_results = search_place(start, end)
    
    # Print search results
    if search_results:
        print("Search Results:")
        for result in search_results:
            print(f"Name: {result['place_name']}, Address: {result['formatted_address']}")
    else:
        print("No results found.")
