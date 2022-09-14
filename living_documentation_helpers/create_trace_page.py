import sys
from os import path
from .template import convert_template
from .userneeds import load_userneeds_from_file
from .feature_file import load_all_feature_files_in_directory, status_to_style
from .collecting_formatter import CollectedFeature, CollectedScenario


def add_scenario_to_userneed(userneeds, userneedId, scenarioId, scenarioName, result):
    userneedId = userneedId.lower()
    for userneed in userneeds:
        if userneed['id'].lower() == userneedId:
            userneed['scenarios'].append({
                'id': scenarioId,
                'name': scenarioName,
                'result': result
            })


def userneed_id_for_scenario(scenario: CollectedScenario):
    for tag in scenario.tags:
        if(tag.lower().startswith('un-')):
            return tag.lower()

    return ''


def id_for_scenario(scenario: CollectedScenario):
    for tag in scenario.tags:
        if(tag.lower().startswith('id-')):
            return tag

    return ''


def main(args=None):
    if args is None:
        args = sys.argv

    if len(args) != 4:
        print('Invalid command format, format is:\n {a[0]} <userneed text file> <path to feature file results> <output file>\n'.format(a=args))
        exit(1)

    userneeds = load_userneeds_from_file(args[1])
    for userneed in userneeds:
        userneed['scenarios'] = []

    features = load_all_feature_files_in_directory(args[2])
    for feature in features:
        for scenario in feature.scenarios:
            userneedId = userneed_id_for_scenario(scenario)
            scenarioId = id_for_scenario(scenario)
            result = scenario.status
            if userneedId != '' and scenarioId != '':
                add_scenario_to_userneed(userneeds, userneedId, scenarioId, feature.name + ' - ' + scenario.name, result)

    context = {
        "userneeds": userneeds,
        "status_to_style": status_to_style
    }

    with open(args[3], 'wt') as file:
        file.write(convert_template('userneeds_trace.jinja2', context))


if __name__ == "__main__":
    main()
