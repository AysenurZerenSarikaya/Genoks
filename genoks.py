import sys
import json
import vcf
import os.path

vcf_reader = vcf.Reader(open(r'C:\Users\SARIKAYA\Desktop\Genoks\example.vcf', 'r'))


vcf_data = []

for record in vcf_reader:
    alt_strs = [str(alt) for alt in record.ALT]
    vcf_data.append({
        'chromosome': record.CHROM,
        'position': record.POS,
        'id': record.ID,
        'reference': record.REF,
        'alternate': alt_strs,
        'quality': record.QUAL,
        'filter': record.FILTER,
        'info': record.INFO,
        'format':record.FORMAT,
        'NA00001':record.samples[0].data,
        'NA00002': record.samples[1].data,
        'NA00003':record.samples[2].data
    })

json_data = json.dumps(vcf_data)

print(json_data)

with open(r'C:\Users\SARIKAYA\Desktop\Genoks\output.json', 'w') as f:
    json.dump(vcf_data, f, indent=4)

#########################################

f = open(r"C:\Users\SARIKAYA\Desktop\Genoks\output.json")

json_load = json.load(f)


if (os.path.isfile(f"{f}") or 1):
    vcard=""
    try:
        for i in range(5):
            chromosome = json_load["chromosome"][i] # needs to be fixed - could be use -> int(my_str)
            position = json_load["position"][i]
            id = json_load["id"][i]
            reference = json_load["reference"][i]
            alternate = json_load["alternate"][i]
            quality = json_load["quality"][i]
            filter = json_load["filter"][i]
            info = json_load["info"][i]
            format = json_load["format"][i]
            nA00001 = json_load["NA00001"][i]
            nA00002 = json_load["NA00002"][i]
            nA00003 = json_load["NA00003"][i]
            vcard += f"""BEGIN:VCARD
VERSION:3.0
CHROM:{chromosome}
POS:{position}
ID:{id}
reference:{reference}
alternate:{alternate}
quality:{quality}
filter:{filter}
info:{info}
format:{format}
NA00001:{nA00001}
NA00002:{nA00002}
NA00003:{nA00003}
END:VCARD
"""
    except IndexError:
        pass
    vcfile="new_output.vcf"
    with open(vcfile, "w",encoding='utf-8') as f:
        f.write(vcard)
    print("VCF file has been generated succesfully")
else:
    print("Json file not found")




















