import xml.etree.ElementTree as etree

def get_element(name) -> str:
    docroot = etree.parse('./assets/elements.xml').getroot()
    treelist = docroot.findall('element')
    xml_data = []
    elements = []

    for elem in treelist:
        elements.append(elem.findtext('name'))
    
    for elem in treelist:
        element = {
            'ID' : elem.get('id'),
            'Symbol': elem.get('symbol'),
            'Period': elem.get('period'),
            'Group' : elem.get('group'),
            'Weight': elem.findtext('weight'),
            'Class' : elem.findtext('class'),
            'Name'  : elem.findtext('name'),
        }

        xml_data.insert(int(element['ID']), element)
    
    proton = 0
    for elem in treelist:
        if elem.findtext('name') != str(name).title():
            proton += 1
        else:
            break
    
    list = []
    try:
        for i in xml_data[proton]:
            list.append(i)
    except IndexError:
        return "error"

    information = []
    for j in list:
        information.append(xml_data[proton][j])

    return information

values = {  
            "amu": "1.66 x 10<sup>-27</sup> kilograms",
            "avogadro": "6.022 x 10^23 molecules",
            "boltzmann": "1.38 x 10<sup>-23</sup> Joule/Kelvin or 1.38 x 10<sup>-16</sup> erg/Kelvin",
            "coulomb": "1/4πε<sub>0</sub> or 9 x 10<sup>9</sup> Newton-meter<sup>2</sup> / Coulomb<sup>2</sup>",
            "electron_charge": "-1.602 x 10<sup>-19</sup> Coulombs",
            "electron_mass": "9.11 x 10<sup>-31</sup> kilograms",
            "gravitational": "6.67 x 10<sup>-11</sup> meter<sup>3</sup>/kilogram-second<sup>2</sup>", 
            "planck": "6.626 x 10<sup>-34</sup> Joule-second", 
            "universal_gas": "8.314 Joule/mole-Kelvin or 0.082 Liter-atmosphere/mole-Kelvin", 
            "wien": "2.9 x 10<sup>-3</sup> meter-Kelvin"
        }

def constant(const):
    if const.lower() not in list(values):
        return "error"
    else:
        return values[const.lower()]