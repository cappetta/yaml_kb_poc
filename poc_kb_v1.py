__author__='cappetta'
import yaml

yaml_file = open('kb_testing_scenario.yaml')
yaml_data = yaml.load_all(yaml_file)

file = open('/tmp/kb_test_file','w')
debug=False


for value in yaml_data:
    print "Complete YAML: %s" % value
    print value.viewkeys()
    if value.has_key("Core_KB"):
        file.write(value["Core_KB"]["name"])
        for kb in value.values():
            print "Core KB -> %s" % kb

    if value.has_key("TestSet1"):
        for tests in value.values():
            for test in tests:
                if test['Vulnerable']:
                    if debug:    print "Test Vulnerable Model: %s " % (test["model"])
                    file.write("\n"+test["model"])
                if not test['Vulnerable']:
                    if debug: print "Test not Vulnerable Version: %s " % (test["version"])
    print "========================="
file.close()
# print "\n"

