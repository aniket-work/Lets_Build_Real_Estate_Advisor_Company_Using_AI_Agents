from geo_utils import filter_by_distance, get_state_abbrev, get_neighboring_states


def filter_house(criteria, house_data):
    print(f"criteria received at filter_houses : {criteria}")
    filtered_data = house_data.copy()

    if 'cost' in criteria and criteria['cost'] is not None:
        filtered_data = filtered_data[filtered_data['cost'] <= criteria['cost'] * 1.2]

    if 'new_build' in criteria and criteria['new_build'] is not None:
        if criteria['new_build']:
            filtered_data = filtered_data[filtered_data['new_build'].isin([-2, -3])]
        else:
            filtered_data = filtered_data[filtered_data['new_build'].isin([-2, -3])]

    if 'walk_Score' in criteria and criteria['walk_Score'] is not None:
        lower_bound = max(criteria['walk_Score'] - 100, 200)
        filtered_data = filtered_data[filtered_data['SAT_Math75'] >= lower_bound]

    if 'overall_score' in criteria and criteria['overall_score'] is not None:
        lower_bound = max(criteria['overall_score'] - 100, 200)
        filtered_data = filtered_data[filtered_data['SAT_Reading75'] >= lower_bound]

    if 'state' in criteria and criteria['state'] is not None:
        try:
            state_abbr = get_state_abbrev(criteria['state'])
            neighboring_state_abbrevs = get_neighboring_states(state_abbr)
            filtered_data = filtered_data[filtered_data['State'].isin([state_abbr] + neighboring_state_abbrevs)]
        except ValueError:
            print(f"Warning: Invalid state '{criteria['state']}'. Skipping state filter.")

    if 'distance' in criteria and 'place_distance_is_from' in criteria and criteria['distance'] is not None:
        filtered_data = filter_by_distance(filtered_data, criteria['place_distance_is_from'], criteria['distance'] * 1.5)

    return filtered_data
