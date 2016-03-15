__author__='cappetta'
import yaml, re, subprocess

# yaml_file = open('kb_testing_scenario.yaml')
yaml_file = open('adobe_testing_scenario.yaml')
yaml_data = yaml.load_all(yaml_file)

file = open('/tmp/kb_header', 'w')
debug=True
kb_prefix_version = ''
kb_prefix_version2 = ''
header = ''
ticket = ''
nasl = '/opt/nessus/bin/nasl'

for value in yaml_data:
    if debug: print "Complete YAML: %s" % value
    if debug: print value.viewkeys()
    if value.has_key("RAW_KB_HEADER"):
        file.write(value["RAW_KB_HEADER"]["name"])
        header = value["RAW_KB_HEADER"]["name"]
        ticket = value["RAW_KB_HEADER"]["ticket"]
        kb_prefix_version = value["kb_prefix_version"]
        kb_prefix_version2 = value["kb_prefix_version2"]

        for kb in value.values():
            if debug: print "Core KB -> %s" % kb

    if value.has_key("TestSet1"):
        for tests in value.values():
            for test in tests:
                if test['Vulnerable']:
                    if debug:
                        kb_version2 = kb_prefix_version2 + str(test["version"]) + "\n"
                        # kb_prefix_model += str(test["version"]) + "\n"
                        version = re.sub('[^A-Za-z0-9\.]','_',str(test["version"])).rstrip('_')
                        kb_version = kb_prefix_version + version
                        tmp_kb = open('/tmp/vuln_'+ str(ticket) + "_" + version ,'w') #todo: need to variablize the attribute lookup
                        print "Test Vulnerable Model: %s Version: %s" % (str(test["version"]), version)#re.sub('[^A-Za-z0-9\.]','_',str(test["version"])))
                        tmp_kb.write(header)
                        tmp_kb.write(kb_version+"\n")
                        tmp_kb.write(kb_version2 + "\n")
                    # header.write(str(test["version"])+"\n")
                if not test['Vulnerable']:
                    if debug: print "Test not Vulnerable Version: %s " % (test["version"])
    print "========================="
file.close()

def get_nasl_files():
    pass

# print "\n"

