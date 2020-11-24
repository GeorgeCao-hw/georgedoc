import oyaml as yaml
import os
import sys

def transferyaml(oldyamlname, newyamlname):
    file_path = os.path.split(os.path.realpath(__file__))[0]

    newyaml_patch = os.path.join(file_path, newyamlname)
    newyaml = open(newyaml_patch, 'w', encoding="utf-8")
    version = {"version": "v1.0"}
    yaml.dump(version, newyaml)

    oldyamlpath = os.path.join(file_path, oldyamlname)

    with open(oldyamlpath, 'r', encoding="utf-8") as yaml_file:
        content = yaml.load(yaml_file.read())
        oldcomm = content["community"]
        community = {"community": oldcomm}
        yaml.dump(community, newyaml)

        repolist = content["repositories"]
        repodata = {}
        repos = []
        for repo in repolist:
            newrepo = {}
            for key in repo.keys():
                if key == 'protected_branches':
                    allbr = []
                    for protectedbr in repo[key]:
                        br = {}
                        br['name'] = protectedbr
                        br['type'] = 'protected'
                        if protectedbr != 'master':
                            br['create_from'] = 'master'
                        allbr.append(br)
                    newrepo['branches'] = allbr
                else:
                    newrepo[key] = repo[key]
            repos.append(newrepo)

        repodata['repositories'] = repos
        yaml.dump(repodata, newyaml)
    return

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Param error, you should like this: \n python transferrepoyaml.py oldfile.yaml newfile.yaml")
        sys.exit()
    oldyamlname = sys.argv[1]
    newyamlname = sys.argv[2]
    transferyaml(oldyamlname, newyamlname)
