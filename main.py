import json
import xml.etree.ElementTree
import sys
import os
import glob

def get_i18n_block(filepath):
    res = ""
    with open(filepath) as in_fh:
        while True:
            line = in_fh.readline()
            if not line: break

            if line.startswith('<i18n'):
                while True:
                    i18n_line = in_fh.readline()
                    if i18n_line.startswith("</"):
                        return res

                    res += i18n_line

def add_sfc_i18n_to_translations(sfc_i18n_json, json_output, prefix):
    for lang in sfc_i18n_json:
        if not lang in json_output:
            json_output[lang] = dict()
        if prefix in json_output[lang]:
            raise ValueError("component %s already exists in %s" % (prefix, lang))
        json_output[lang][prefix] = sfc_i18n_json[lang]

def extract_from_file(filepath, output_json):
    i18n_str = get_i18n_block(filepath)
    if not i18n_str:
        return
    i18n_json = json.loads(i18n_str)
    add_sfc_i18n_to_translations(i18n_json, output_json, os.path.basename(filepath))

def main():
    if len(sys.argv) != 2:
        print("NOOOOOOOOO!")
        exit(1)
    else:
        new_json = dict()
        for filename in glob.iglob(os.path.join(sys.argv[1], "./**/*.vue"), recursive=True):
            extract_from_file(filename, new_json)
        res_str = json.dumps(new_json, ensure_ascii=False)
        print(res_str)


if __name__ == "__main__":
    main()