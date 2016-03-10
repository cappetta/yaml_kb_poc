__author__='cappetta'
import yaml

yaml_file = open('kb_testing_scenario.yaml')
yaml_data = yaml.load_all(yaml_file)

for value in yaml_data:
# works for single YAML
        # print "Individual Static KBs"
        # for static_kb in value['Static_KB']:
        #         print static_kb
        # for dyn_kb in value['Dynamic_KB']['version']:
        #        print dyn_kb

# Broken
#         for k,v in value.items():
#                 print k, "->", v
#                 for val in v:
#                         # print "val => ", val
#                         for att in val:
#                                 print "att => ", att
#                                 for asset in att:
#                                         print "asset => ", asset

    print "YAML: %s" % value
    for tests in value.values():
        # print "YAML Test: %s" % tests
        for test in tests:
            if test['Vulnerable']:
                print "Test Vulnerability: %s "  % (test["kb"])
            if not test['Vulnerable']:
                print "Test not Vulnerable: %s "  % (test["kb"])


print "\n"

