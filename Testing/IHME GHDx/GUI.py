import tkinter as tk

# Define the JavaScript object hierarchy
js_obj = {
  "All causes": {
    "children": {},
    "id": 294,
    "cause": "Total",
    "name": "All causes",
    "medium_name": "All causes",
    "short_name": "All causes",
    "most_detailed": 0,
    "male": 1,
    "female": 1,
    "sort_order": 1
  },
  "Communicable, maternal, neonatal, and nutritional diseases": {
    "children": {
      "Respiratory infections and tuberculosis": {
        "children": {
          "Tuberculosis": {
            "children": {
              "Drug-susceptible tuberculosis": {
                "children": {},
                "id": 934,
                "cause": "A.2.1.2",
                "name": "Drug-susceptible tuberculosis",
                "medium_name": "Drug-susceptible TB",
                "short_name": "Drug-Sus TB",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 19
              },
              "Multidrug-resistant tuberculosis without extensive drug resistance": {
                "children": {},
                "id": 946,
                "cause": "A.2.1.3",
                "name": "Multidrug-resistant tuberculosis without extensive drug resistance",
                "medium_name": "MDR-TB without XDR",
                "short_name": "MDR-TB",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 20
              },
              "Extensively drug-resistant tuberculosis": {
                "children": {},
                "id": 947,
                "cause": "A.2.1.4",
                "name": "Extensively drug-resistant tuberculosis",
                "medium_name": "XDR-TB only",
                "short_name": "XDR-TB",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 21
              },
              "Latent tuberculosis infection": {
                "children": {},
                "id": 954,
                "cause": "A.2.1.1",
                "name": "Latent tuberculosis infection",
                "medium_name": "Latent TB infection",
                "short_name": "LTBI",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 18
              }
            },
            "id": 297,
            "cause": "A.2.1",
            "name": "Tuberculosis",
            "medium_name": "Tuberculosis",
            "short_name": "TB",
            "most_detailed": 0,
            "male": 1,
            "female": 1,
            "sort_order": 17
          },
          "Lower respiratory infections": {
            "children": {},
            "id": 322,
            "cause": "A.2.2",
            "name": "Lower respiratory infections",
            "medium_name": "Lower respiratory infect",
            "short_name": "LRI",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 22
          },
          "Upper respiratory infections": {
            "children": {},
            "id": 328,
            "cause": "A.2.3",
            "name": "Upper respiratory infections",
            "medium_name": "Upper respiratory infect",
            "short_name": "URI",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 23
          },
          "Otitis media": {
            "children": {},
            "id": 329,
            "cause": "A.2.4",
            "name": "Otitis media",
            "medium_name": "Otitis media",
            "short_name": "Otitis",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 24
          }
        },
        "id": 956,
        "cause": "A.2",
        "name": "Respiratory infections and tuberculosis",
        "medium_name": "Respiratory infections & TB",
        "short_name": "Resp+TB",
        "most_detailed": 0,
        "male": 1,
        "female": 1,
        "sort_order": 16
      },
      "HIV/AIDS and sexually transmitted infections": {
        "children": {
          "HIV/AIDS": {
            "children": {
              "HIV/AIDS resulting in other diseases": {
                "children": {},
                "id": 300,
                "cause": "A.1.1.4",
                "name": "HIV/AIDS resulting in other diseases",
                "medium_name": "HIV/AIDS other",
                "short_name": "Oth HIV",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 8
              },
              "HIV/AIDS - Drug-susceptible Tuberculosis": {
                "children": {},
                "id": 948,
                "cause": "A.1.1.1",
                "name": "HIV/AIDS - Drug-susceptible Tuberculosis",
                "medium_name": "Drug-susceptible HIV/AIDS - TB",
                "short_name": "Drug-Sus HIV-TB",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 5
              },
              "HIV/AIDS - Multidrug-resistant Tuberculosis without extensive drug resistance": {
                "children": {},
                "id": 949,
                "cause": "A.1.1.2",
                "name": "HIV/AIDS - Multidrug-resistant Tuberculosis without extensive drug resistance",
                "medium_name": "MDR-HIV/AIDS-TB without XDR",
                "short_name": "MDR-HIV-TB",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 6
              },
              "HIV/AIDS - Extensively drug-resistant Tuberculosis": {
                "children": {},
                "id": 950,
                "cause": "A.1.1.3",
                "name": "HIV/AIDS - Extensively drug-resistant Tuberculosis",
                "medium_name": "XDR HIV/AIDS-TB",
                "short_name": "XDR-HIV-TB",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 7
              }
            },
            "id": 298,
            "cause": "A.1.1",
            "name": "HIV/AIDS",
            "medium_name": "HIV/AIDS",
            "short_name": "HIV",
            "most_detailed": 0,
            "male": 1,
            "female": 1,
            "sort_order": 4
          },
          "Sexually transmitted infections excluding HIV": {
            "children": {
              "Syphilis": {
                "children": {},
                "id": 394,
                "cause": "A.1.2.1",
                "name": "Syphilis",
                "medium_name": "Syphilis",
                "short_name": "Syphilis",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 10
              },
              "Chlamydial infection": {
                "children": {},
                "id": 395,
                "cause": "A.1.2.2",
                "name": "Chlamydial infection",
                "medium_name": "Chlamydia",
                "short_name": "Chlamydia",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 11
              },
              "Gonococcal infection": {
                "children": {},
                "id": 396,
                "cause": "A.1.2.3",
                "name": "Gonococcal infection",
                "medium_name": "Gonorrhea",
                "short_name": "Gonorrhea",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 12
              },
              "Trichomoniasis": {
                "children": {},
                "id": 397,
                "cause": "A.1.2.4",
                "name": "Trichomoniasis",
                "medium_name": "Trichomoniasis",
                "short_name": "Trich",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 13
              },
              "Genital herpes": {
                "children": {},
                "id": 398,
                "cause": "A.1.2.5",
                "name": "Genital herpes",
                "medium_name": "Genital herpes",
                "short_name": "Herpes",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 14
              },
              "Other sexually transmitted infections": {
                "children": {},
                "id": 399,
                "cause": "A.1.2.6",
                "name": "Other sexually transmitted infections",
                "medium_name": "Other STIs",
                "short_name": "Oth STI",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 15
              }
            },
            "id": 393,
            "cause": "A.1.2",
            "name": "Sexually transmitted infections excluding HIV",
            "medium_name": "STIs",
            "short_name": "STI",
            "most_detailed": 0,
            "male": 1,
            "female": 1,
            "sort_order": 9
          }
        },
        "id": 955,
        "cause": "A.1",
        "name": "HIV/AIDS and sexually transmitted infections",
        "medium_name": "HIV/AIDS & STIs",
        "short_name": "HIV/AIDS+STIs",
        "most_detailed": 0,
        "male": 1,
        "female": 1,
        "sort_order": 3
      },
      "Enteric infections": {
        "children": {
          "Diarrheal diseases": {
            "children": {},
            "id": 302,
            "cause": "A.3.1",
            "name": "Diarrheal diseases",
            "medium_name": "Diarrheal diseases",
            "short_name": "Diarrhea",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 26
          },
          "Typhoid and paratyphoid": {
            "children": {
              "Typhoid fever": {
                "children": {},
                "id": 319,
                "cause": "A.3.2.1",
                "name": "Typhoid fever",
                "medium_name": "Typhoid fever",
                "short_name": "Typhoid",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 28
              },
              "Paratyphoid fever": {
                "children": {},
                "id": 320,
                "cause": "A.3.2.2",
                "name": "Paratyphoid fever",
                "medium_name": "Paratyphoid fever",
                "short_name": "Paratyph",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 29
              }
            },
            "id": 958,
            "cause": "A.3.2",
            "name": "Typhoid and paratyphoid",
            "medium_name": "Typhoid & paratyph",
            "short_name": "Typh + Paratyph",
            "most_detailed": 0,
            "male": 1,
            "female": 1,
            "sort_order": 27
          },
          "Other intestinal infectious diseases": {
            "children": {},
            "id": 321,
            "cause": "A.3.4",
            "name": "Other intestinal infectious diseases",
            "medium_name": "Other intestinal infect",
            "short_name": "Oth Intest",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 31
          },
          "Invasive Non-typhoidal Salmonella (iNTS)": {
            "children": {},
            "id": 959,
            "cause": "A.3.3",
            "name": "Invasive Non-typhoidal Salmonella (iNTS)",
            "medium_name": "iNTS",
            "short_name": "iNTS",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 30
          }
        },
        "id": 957,
        "cause": "A.3",
        "name": "Enteric infections",
        "medium_name": "Enteric infections",
        "short_name": "Enteric Infect",
        "most_detailed": 0,
        "male": 1,
        "female": 1,
        "sort_order": 25
      },
      "Other infectious diseases": {
        "children": {
          "Meningitis": {
            "children": {},
            "id": 332,
            "cause": "A.5.1",
            "name": "Meningitis",
            "medium_name": "Meningitis",
            "short_name": "Meningitis",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 59
          },
          "Encephalitis": {
            "children": {},
            "id": 337,
            "cause": "A.5.2",
            "name": "Encephalitis",
            "medium_name": "Encephalitis",
            "short_name": "Encepha",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 60
          },
          "Diphtheria": {
            "children": {},
            "id": 338,
            "cause": "A.5.3",
            "name": "Diphtheria",
            "medium_name": "Diphtheria",
            "short_name": "Diphtheria",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 61
          },
          "Whooping cough": {
            "children": {},
            "id": 339,
            "cause": "A.5.4",
            "name": "Whooping cough",
            "medium_name": "Whooping cough",
            "short_name": "Whooping",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 62
          },
          "Tetanus": {
            "children": {},
            "id": 340,
            "cause": "A.5.5",
            "name": "Tetanus",
            "medium_name": "Tetanus",
            "short_name": "Tetanus",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 63
          },
          "Measles": {
            "children": {},
            "id": 341,
            "cause": "A.5.6",
            "name": "Measles",
            "medium_name": "Measles",
            "short_name": "Measles",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 64
          },
          "Varicella and herpes zoster": {
            "children": {},
            "id": 342,
            "cause": "A.5.7",
            "name": "Varicella and herpes zoster",
            "medium_name": "Varicella",
            "short_name": "Varicella",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 65
          },
          "Acute hepatitis": {
            "children": {
              "Acute hepatitis A": {
                "children": {},
                "id": 401,
                "cause": "A.5.8.1",
                "name": "Acute hepatitis A",
                "medium_name": "Acute hepatitis A",
                "short_name": "Hep A",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 67
              },
              "Acute hepatitis B": {
                "children": {},
                "id": 402,
                "cause": "A.5.8.2",
                "name": "Acute hepatitis B",
                "medium_name": "Acute hepatitis B",
                "short_name": "Hep B",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 68
              },
              "Acute hepatitis C": {
                "children": {},
                "id": 403,
                "cause": "A.5.8.3",
                "name": "Acute hepatitis C",
                "medium_name": "Acute hepatitis C",
                "short_name": "Hep C",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 69
              },
              "Acute hepatitis E": {
                "children": {},
                "id": 404,
                "cause": "A.5.8.4",
                "name": "Acute hepatitis E",
                "medium_name": "Acute hepatitis E",
                "short_name": "Hep E",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 70
              }
            },
            "id": 400,
            "cause": "A.5.8",
            "name": "Acute hepatitis",
            "medium_name": "Acute hepatitis",
            "short_name": "Hep",
            "most_detailed": 0,
            "male": 1,
            "female": 1,
            "sort_order": 66
          },
          "Other unspecified infectious diseases": {
            "children": {},
            "id": 408,
            "cause": "A.5.9",
            "name": "Other unspecified infectious diseases",
            "medium_name": "Other unspecified infectious",
            "short_name": "Oth Un Inf",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 71
          }
        },
        "id": 961,
        "cause": "A.5",
        "name": "Other infectious diseases",
        "medium_name": "Other infectious",
        "short_name": "Other+Diseases",
        "most_detailed": 0,
        "male": 1,
        "female": 1,
        "sort_order": 58
      },
      "Neglected tropical diseases and malaria": {
        "children": {
          "Malaria": {
            "children": {},
            "id": 345,
            "cause": "A.4.1",
            "name": "Malaria",
            "medium_name": "Malaria",
            "short_name": "Malaria",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 33
          },
          "Chagas disease": {
            "children": {},
            "id": 346,
            "cause": "A.4.2",
            "name": "Chagas disease",
            "medium_name": "Chagas disease",
            "short_name": "Chagas",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 34
          },
          "Leishmaniasis": {
            "children": {
              "Visceral leishmaniasis": {
                "children": {},
                "id": 348,
                "cause": "A.4.3.1",
                "name": "Visceral leishmaniasis",
                "medium_name": "Visceral leishmaniasis",
                "short_name": "Vis Leish",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 36
              },
              "Cutaneous and mucocutaneous leishmaniasis": {
                "children": {},
                "id": 349,
                "cause": "A.4.3.2",
                "name": "Cutaneous and mucocutaneous leishmaniasis",
                "medium_name": "Cutaneous leishmaniasis",
                "short_name": "Cut Leish",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 37
              }
            },
            "id": 347,
            "cause": "A.4.3",
            "name": "Leishmaniasis",
            "medium_name": "Leishmaniasis",
            "short_name": "Leish",
            "most_detailed": 0,
            "male": 1,
            "female": 1,
            "sort_order": 35
          },
          "African trypanosomiasis": {
            "children": {},
            "id": 350,
            "cause": "A.4.4",
            "name": "African trypanosomiasis",
            "medium_name": "African trypanosomiasis",
            "short_name": "Afr Tryp",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 38
          },
          "Schistosomiasis": {
            "children": {},
            "id": 351,
            "cause": "A.4.5",
            "name": "Schistosomiasis",
            "medium_name": "Schistosomiasis",
            "short_name": "Schisto",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 39
          },
          "Cysticercosis": {
            "children": {},
            "id": 352,
            "cause": "A.4.6",
            "name": "Cysticercosis",
            "medium_name": "Cysticercosis",
            "short_name": "Cysticer",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 40
          },
          "Cystic echinococcosis": {
            "children": {},
            "id": 353,
            "cause": "A.4.7",
            "name": "Cystic echinococcosis",
            "medium_name": "Cystic echinococcosis",
            "short_name": "Echino",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 41
          },
          "Lymphatic filariasis": {
            "children": {},
            "id": 354,
            "cause": "A.4.8",
            "name": "Lymphatic filariasis",
            "medium_name": "Lymphatic filariasis",
            "short_name": "LF",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 42
          },
          "Onchocerciasis": {
            "children": {},
            "id": 355,
            "cause": "A.4.9",
            "name": "Onchocerciasis",
            "medium_name": "Onchocerciasis",
            "short_name": "Oncho",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 43
          },
          "Trachoma": {
            "children": {},
            "id": 356,
            "cause": "A.4.10",
            "name": "Trachoma",
            "medium_name": "Trachoma",
            "short_name": "Trachoma",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 44
          },
          "Dengue": {
            "children": {},
            "id": 357,
            "cause": "A.4.11",
            "name": "Dengue",
            "medium_name": "Dengue",
            "short_name": "Dengue",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 45
          },
          "Yellow fever": {
            "children": {},
            "id": 358,
            "cause": "A.4.12",
            "name": "Yellow fever",
            "medium_name": "Yellow fever",
            "short_name": "Yellow Fev",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 46
          },
          "Rabies": {
            "children": {},
            "id": 359,
            "cause": "A.4.13",
            "name": "Rabies",
            "medium_name": "Rabies",
            "short_name": "Rabies",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 47
          },
          "Intestinal nematode infections": {
            "children": {
              "Ascariasis": {
                "children": {},
                "id": 361,
                "cause": "A.4.14.1",
                "name": "Ascariasis",
                "medium_name": "Ascariasis",
                "short_name": "Ascaria",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 49
              },
              "Trichuriasis": {
                "children": {},
                "id": 362,
                "cause": "A.4.14.2",
                "name": "Trichuriasis",
                "medium_name": "Trichuriasis",
                "short_name": "Trichuria",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 50
              },
              "Hookworm disease": {
                "children": {},
                "id": 363,
                "cause": "A.4.14.3",
                "name": "Hookworm disease",
                "medium_name": "Hookworm disease",
                "short_name": "Hookworm",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 51
              }
            },
            "id": 360,
            "cause": "A.4.14",
            "name": "Intestinal nematode infections",
            "medium_name": "Intestinal nematode",
            "short_name": "Nematode",
            "most_detailed": 0,
            "male": 1,
            "female": 1,
            "sort_order": 48
          },
          "Food-borne trematodiases": {
            "children": {},
            "id": 364,
            "cause": "A.4.15",
            "name": "Food-borne trematodiases",
            "medium_name": "Food-borne trematodiases",
            "short_name": "FB Trema",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 52
          },
          "Other neglected tropical diseases": {
            "children": {},
            "id": 365,
            "cause": "A.4.20",
            "name": "Other neglected tropical diseases",
            "medium_name": "Other NTDs",
            "short_name": "Oth NTD",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 57
          },
          "Leprosy": {
            "children": {},
            "id": 405,
            "cause": "A.4.16",
            "name": "Leprosy",
            "medium_name": "Leprosy",
            "short_name": "Leprosy",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 53
          },
          "Ebola": {
            "children": {},
            "id": 843,
            "cause": "A.4.17",
            "name": "Ebola",
            "medium_name": "Ebola",
            "short_name": "Ebola",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 54
          },
          "Zika virus": {
            "children": {},
            "id": 935,
            "cause": "A.4.18",
            "name": "Zika virus",
            "medium_name": "Zika virus",
            "short_name": "Zika",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 55
          },
          "Guinea worm disease": {
            "children": {},
            "id": 936,
            "cause": "A.4.19",
            "name": "Guinea worm disease",
            "medium_name": "Guinea worm",
            "short_name": "GWD",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 56
          }
        },
        "id": 344,
        "cause": "A.4",
        "name": "Neglected tropical diseases and malaria",
        "medium_name": "NTDs & malaria",
        "short_name": "NTD+Malaria",
        "most_detailed": 0,
        "male": 1,
        "female": 1,
        "sort_order": 32
      },
      "Maternal and neonatal disorders": {
        "children": {
          "Maternal disorders": {
            "children": {
              "Maternal hemorrhage": {
                "children": {},
                "id": 367,
                "cause": "A.6.1.1",
                "name": "Maternal hemorrhage",
                "medium_name": "Maternal hemorrhage",
                "short_name": "Mat Hem",
                "most_detailed": 1,
                "male": 0,
                "female": 1,
                "sort_order": 74
              },
              "Maternal sepsis and other maternal infections": {
                "children": {},
                "id": 368,
                "cause": "A.6.1.2",
                "name": "Maternal sepsis and other maternal infections",
                "medium_name": "Maternal sepsis",
                "short_name": "Mat Sepsis",
                "most_detailed": 1,
                "male": 0,
                "female": 1,
                "sort_order": 75
              },
              "Maternal hypertensive disorders": {
                "children": {},
                "id": 369,
                "cause": "A.6.1.3",
                "name": "Maternal hypertensive disorders",
                "medium_name": "Maternal hypertension",
                "short_name": "Mat HTN",
                "most_detailed": 1,
                "male": 0,
                "female": 1,
                "sort_order": 76
              },
              "Maternal obstructed labor and uterine rupture": {
                "children": {},
                "id": 370,
                "cause": "A.6.1.4",
                "name": "Maternal obstructed labor and uterine rupture",
                "medium_name": "Obstructed labor",
                "short_name": "Obst Labor",
                "most_detailed": 1,
                "male": 0,
                "female": 1,
                "sort_order": 77
              },
              "Ectopic pregnancy": {
                "children": {},
                "id": 374,
                "cause": "A.6.1.6",
                "name": "Ectopic pregnancy",
                "medium_name": "Ectopic pregnancy",
                "short_name": "Ectopic Preg",
                "most_detailed": 1,
                "male": 0,
                "female": 1,
                "sort_order": 79
              },
              "Indirect maternal deaths": {
                "children": {},
                "id": 375,
                "cause": "A.6.1.7",
                "name": "Indirect maternal deaths",
                "medium_name": "Maternal indirect",
                "short_name": "Mat Indir",
                "most_detailed": 1,
                "male": 0,
                "female": 1,
                "sort_order": 80
              },
              "Late maternal deaths": {
                "children": {},
                "id": 376,
                "cause": "A.6.1.8",
                "name": "Late maternal deaths",
                "medium_name": "Maternal late",
                "short_name": "Mat Late",
                "most_detailed": 1,
                "male": 0,
                "female": 1,
                "sort_order": 81
              },
              "Other maternal disorders": {
                "children": {},
                "id": 379,
                "cause": "A.6.1.10",
                "name": "Other maternal disorders",
                "medium_name": "Other maternal disorders",
                "short_name": "Oth Mat",
                "most_detailed": 1,
                "male": 0,
                "female": 1,
                "sort_order": 83
              },
              "Maternal deaths aggravated by HIV/AIDS": {
                "children": {},
                "id": 741,
                "cause": "A.6.1.9",
                "name": "Maternal deaths aggravated by HIV/AIDS",
                "medium_name": "Maternal HIV",
                "short_name": "Mat HIV",
                "most_detailed": 1,
                "male": 0,
                "female": 1,
                "sort_order": 82
              },
              "Maternal abortion and miscarriage": {
                "children": {},
                "id": 995,
                "cause": "A.6.1.5",
                "name": "Maternal abortion and miscarriage",
                "medium_name": "Maternal abortion miscarriage",
                "short_name": "Mat Abort",
                "most_detailed": 1,
                "male": 0,
                "female": 1,
                "sort_order": 78
              }
            },
            "id": 366,
            "cause": "A.6.1",
            "name": "Maternal disorders",
            "medium_name": "Maternal disorders",
            "short_name": "Maternal",
            "most_detailed": 0,
            "male": 0,
            "female": 1,
            "sort_order": 73
          },
          "Neonatal disorders": {
            "children": {
              "Neonatal preterm birth": {
                "children": {},
                "id": 381,
                "cause": "A.6.2.1",
                "name": "Neonatal preterm birth",
                "medium_name": "Neonatal preterm birth",
                "short_name": "NN Preterm",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 85
              },
              "Neonatal encephalopathy due to birth asphyxia and trauma": {
                "children": {},
                "id": 382,
                "cause": "A.6.2.2",
                "name": "Neonatal encephalopathy due to birth asphyxia and trauma",
                "medium_name": "Neonatal encephalopathy",
                "short_name": "NN Enceph",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 86
              },
              "Neonatal sepsis and other neonatal infections": {
                "children": {},
                "id": 383,
                "cause": "A.6.2.3",
                "name": "Neonatal sepsis and other neonatal infections",
                "medium_name": "Neonatal sepsis",
                "short_name": "NN Sepsis",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 87
              },
              "Hemolytic disease and other neonatal jaundice": {
                "children": {},
                "id": 384,
                "cause": "A.6.2.4",
                "name": "Hemolytic disease and other neonatal jaundice",
                "medium_name": "Neonatal hemolytic",
                "short_name": "NN Hemol",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 88
              },
              "Other neonatal disorders": {
                "children": {},
                "id": 385,
                "cause": "A.6.2.5",
                "name": "Other neonatal disorders",
                "medium_name": "Other neonatal",
                "short_name": "Oth NN",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 89
              }
            },
            "id": 380,
            "cause": "A.6.2",
            "name": "Neonatal disorders",
            "medium_name": "Neonatal disorders",
            "short_name": "Neonatal",
            "most_detailed": 0,
            "male": 1,
            "female": 1,
            "sort_order": 84
          }
        },
        "id": 962,
        "cause": "A.6",
        "name": "Maternal and neonatal disorders",
        "medium_name": "Maternal & neonatal",
        "short_name": "Mat+Neonat",
        "most_detailed": 0,
        "male": 1,
        "female": 1,
        "sort_order": 72
      },
      "Nutritional deficiencies": {
        "children": {
          "Protein-energy malnutrition": {
            "children": {},
            "id": 387,
            "cause": "A.7.1",
            "name": "Protein-energy malnutrition",
            "medium_name": "Protein-energy malnutrition",
            "short_name": "PEM",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 91
          },
          "Iodine deficiency": {
            "children": {},
            "id": 388,
            "cause": "A.7.2",
            "name": "Iodine deficiency",
            "medium_name": "Iodine deficiency",
            "short_name": "Iodine",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 92
          },
          "Vitamin A deficiency": {
            "children": {},
            "id": 389,
            "cause": "A.7.3",
            "name": "Vitamin A deficiency",
            "medium_name": "Vitamin A deficiency",
            "short_name": "Vit A",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 93
          },
          "Dietary iron deficiency": {
            "children": {},
            "id": 390,
            "cause": "A.7.4",
            "name": "Dietary iron deficiency",
            "medium_name": "Dietary iron deficiency",
            "short_name": "Iron",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 94
          },
          "Other nutritional deficiencies": {
            "children": {},
            "id": 391,
            "cause": "A.7.5",
            "name": "Other nutritional deficiencies",
            "medium_name": "Other nutritional",
            "short_name": "Oth Nutr",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 95
          }
        },
        "id": 386,
        "cause": "A.7",
        "name": "Nutritional deficiencies",
        "medium_name": "Nutritional deficiencies",
        "short_name": "Nutr Def",
        "most_detailed": 0,
        "male": 1,
        "female": 1,
        "sort_order": 90
      }
    },
    "id": 295,
    "cause": "A",
    "name": "Communicable, maternal, neonatal, and nutritional diseases",
    "medium_name": "Group I",
    "short_name": "Group I",
    "most_detailed": 0,
    "male": 1,
    "female": 1,
    "sort_order": 2
  },
  "Non-communicable diseases": {
    "children": {
      "Neoplasms": {
        "children": {
          "Esophageal cancer": {
            "children": {},
            "id": 411,
            "cause": "B.1.4",
            "name": "Esophageal cancer",
            "medium_name": "Esophageal cancer",
            "short_name": "Esophag C",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 101
          },
          "Stomach cancer": {
            "children": {},
            "id": 414,
            "cause": "B.1.5",
            "name": "Stomach cancer",
            "medium_name": "Stomach cancer",
            "short_name": "Stomach C",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 102
          },
          "Liver cancer": {
            "children": {
              "Liver cancer due to hepatitis B": {
                "children": {},
                "id": 418,
                "cause": "B.1.7.1",
                "name": "Liver cancer due to hepatitis B",
                "medium_name": "Liver cancer hepatitis B",
                "short_name": "Liver C HepB",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 105
              },
              "Liver cancer due to hepatitis C": {
                "children": {},
                "id": 419,
                "cause": "B.1.7.2",
                "name": "Liver cancer due to hepatitis C",
                "medium_name": "Liver cancer hepatitis C",
                "short_name": "Liver C HepC",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 106
              },
              "Liver cancer due to alcohol use": {
                "children": {},
                "id": 420,
                "cause": "B.1.7.3",
                "name": "Liver cancer due to alcohol use",
                "medium_name": "Liver cancer alcohol",
                "short_name": "Liver C Alc",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 107
              },
              "Liver cancer due to NASH": {
                "children": {},
                "id": 996,
                "cause": "B.1.7.4",
                "name": "Liver cancer due to NASH",
                "medium_name": "Liver cancer due to NASH",
                "short_name": "Liver C NASH",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 108
              },
              "Liver cancer due to other causes": {
                "children": {},
                "id": 1021,
                "cause": "B.1.7.5",
                "name": "Liver cancer due to other causes",
                "medium_name": "Liver cancer other",
                "short_name": "Oth Liver C",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 109
              }
            },
            "id": 417,
            "cause": "B.1.7",
            "name": "Liver cancer",
            "medium_name": "Liver cancer",
            "short_name": "Liver C",
            "most_detailed": 0,
            "male": 1,
            "female": 1,
            "sort_order": 104
          },
          "Larynx cancer": {
            "children": {},
            "id": 423,
            "cause": "B.1.10",
            "name": "Larynx cancer",
            "medium_name": "Larynx cancer",
            "short_name": "Larynx C",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 112
          },
          "Tracheal, bronchus, and lung cancer": {
            "children": {},
            "id": 426,
            "cause": "B.1.11",
            "name": "Tracheal, bronchus, and lung cancer",
            "medium_name": "Lung cancer",
            "short_name": "Lung C",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 113
          },
          "Breast cancer": {
            "children": {},
            "id": 429,
            "cause": "B.1.14",
            "name": "Breast cancer",
            "medium_name": "Breast cancer",
            "short_name": "Breast C",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 118
          },
          "Cervical cancer": {
            "children": {},
            "id": 432,
            "cause": "B.1.15",
            "name": "Cervical cancer",
            "medium_name": "Cervical cancer",
            "short_name": "Cervix C",
            "most_detailed": 1,
            "male": 0,
            "female": 1,
            "sort_order": 119
          },
          "Uterine cancer": {
            "children": {},
            "id": 435,
            "cause": "B.1.16",
            "name": "Uterine cancer",
            "medium_name": "Uterine cancer",
            "short_name": "Uterus C",
            "most_detailed": 1,
            "male": 0,
            "female": 1,
            "sort_order": 120
          },
          "Prostate cancer": {
            "children": {},
            "id": 438,
            "cause": "B.1.18",
            "name": "Prostate cancer",
            "medium_name": "Prostate cancer",
            "short_name": "Prostate C",
            "most_detailed": 1,
            "male": 1,
            "female": 0,
            "sort_order": 122
          },
          "Colon and rectum cancer": {
            "children": {},
            "id": 441,
            "cause": "B.1.6",
            "name": "Colon and rectum cancer",
            "medium_name": "Colorectal cancer",
            "short_name": "Colorect C",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 103
          },
          "Lip and oral cavity cancer": {
            "children": {},
            "id": 444,
            "cause": "B.1.1",
            "name": "Lip and oral cavity cancer",
            "medium_name": "Lip oral cavity cancer",
            "short_name": "Lip Oral C",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 98
          },
          "Nasopharynx cancer": {
            "children": {},
            "id": 447,
            "cause": "B.1.2",
            "name": "Nasopharynx cancer",
            "medium_name": "Nasopharynx cancer",
            "short_name": "Nasoph C",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 99
          },
          "Other pharynx cancer": {
            "children": {},
            "id": 450,
            "cause": "B.1.3",
            "name": "Other pharynx cancer",
            "medium_name": "Other pharynx cancer",
            "short_name": "Oth Phar C",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 100
          },
          "Gallbladder and biliary tract cancer": {
            "children": {},
            "id": 453,
            "cause": "B.1.8",
            "name": "Gallbladder and biliary tract cancer",
            "medium_name": "Gallbladder cancer",
            "short_name": "Gallblad C",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 110
          },
          "Pancreatic cancer": {
            "children": {},
            "id": 456,
            "cause": "B.1.9",
            "name": "Pancreatic cancer",
            "medium_name": "Pancreatic cancer",
            "short_name": "Pancreas C",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 111
          },
          "Malignant skin melanoma": {
            "children": {},
            "id": 459,
            "cause": "B.1.12",
            "name": "Malignant skin melanoma",
            "medium_name": "Melanoma",
            "short_name": "Melanoma",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 114
          },
          "Non-melanoma skin cancer": {
            "children": {
              "Non-melanoma skin cancer (squamous-cell carcinoma)": {
                "children": {},
                "id": 849,
                "cause": "B.1.13.1",
                "name": "Non-melanoma skin cancer (squamous-cell carcinoma)",
                "medium_name": "Skin cancer SCC",
                "short_name": "SCC",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 116
              },
              "Non-melanoma skin cancer (basal-cell carcinoma)": {
                "children": {},
                "id": 850,
                "cause": "B.1.13.2",
                "name": "Non-melanoma skin cancer (basal-cell carcinoma)",
                "medium_name": "Skin cancer BCC",
                "short_name": "BCC",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 117
              }
            },
            "id": 462,
            "cause": "B.1.13",
            "name": "Non-melanoma skin cancer",
            "medium_name": "Skin cancer",
            "short_name": "Skin C",
            "most_detailed": 0,
            "male": 1,
            "female": 1,
            "sort_order": 115
          },
          "Ovarian cancer": {
            "children": {},
            "id": 465,
            "cause": "B.1.17",
            "name": "Ovarian cancer",
            "medium_name": "Ovarian cancer",
            "short_name": "Ovary C",
            "most_detailed": 1,
            "male": 0,
            "female": 1,
            "sort_order": 121
          },
          "Testicular cancer": {
            "children": {},
            "id": 468,
            "cause": "B.1.19",
            "name": "Testicular cancer",
            "medium_name": "Testicular cancer",
            "short_name": "Testis C",
            "most_detailed": 1,
            "male": 1,
            "female": 0,
            "sort_order": 123
          },
          "Kidney cancer": {
            "children": {},
            "id": 471,
            "cause": "B.1.20",
            "name": "Kidney cancer",
            "medium_name": "Kidney cancer",
            "short_name": "Kidney C",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 124
          },
          "Bladder cancer": {
            "children": {},
            "id": 474,
            "cause": "B.1.21",
            "name": "Bladder cancer",
            "medium_name": "Bladder cancer",
            "short_name": "Bladder C",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 125
          },
          "Brain and central nervous system cancer": {
            "children": {},
            "id": 477,
            "cause": "B.1.22",
            "name": "Brain and central nervous system cancer",
            "medium_name": "Brain cancer",
            "short_name": "Brain C",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 126
          },
          "Thyroid cancer": {
            "children": {},
            "id": 480,
            "cause": "B.1.23",
            "name": "Thyroid cancer",
            "medium_name": "Thyroid cancer",
            "short_name": "Thyroid C",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 127
          },
          "Mesothelioma": {
            "children": {},
            "id": 483,
            "cause": "B.1.24",
            "name": "Mesothelioma",
            "medium_name": "Mesothelioma",
            "short_name": "Mesothel",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 128
          },
          "Hodgkin lymphoma": {
            "children": {},
            "id": 484,
            "cause": "B.1.25",
            "name": "Hodgkin lymphoma",
            "medium_name": "Hodgkin lymphoma",
            "short_name": "Hodgkin",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 129
          },
          "Non-Hodgkin lymphoma": {
            "children": {},
            "id": 485,
            "cause": "B.1.26",
            "name": "Non-Hodgkin lymphoma",
            "medium_name": "Lymphoma",
            "short_name": "Lymphoma",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 130
          },
          "Multiple myeloma": {
            "children": {},
            "id": 486,
            "cause": "B.1.27",
            "name": "Multiple myeloma",
            "medium_name": "Myeloma",
            "short_name": "Myeloma",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 131
          },
          "Leukemia": {
            "children": {
              "Acute lymphoid leukemia": {
                "children": {},
                "id": 845,
                "cause": "B.1.28.1",
                "name": "Acute lymphoid leukemia",
                "medium_name": "Acute lymphoid leukemia",
                "short_name": "ALL",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 133
              },
              "Chronic lymphoid leukemia": {
                "children": {},
                "id": 846,
                "cause": "B.1.28.2",
                "name": "Chronic lymphoid leukemia",
                "medium_name": "Chronic lymphoid leukemia",
                "short_name": "CLL",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 134
              },
              "Acute myeloid leukemia": {
                "children": {},
                "id": 847,
                "cause": "B.1.28.3",
                "name": "Acute myeloid leukemia",
                "medium_name": "Acute myeloid leukemia",
                "short_name": "AML",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 135
              },
              "Chronic myeloid leukemia": {
                "children": {},
                "id": 848,
                "cause": "B.1.28.4",
                "name": "Chronic myeloid leukemia",
                "medium_name": "Chronic myeloid leukemia",
                "short_name": "CML",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 136
              },
              "Other leukemia": {
                "children": {},
                "id": 943,
                "cause": "B.1.28.5",
                "name": "Other leukemia",
                "medium_name": "Other leukemia",
                "short_name": "Oth Leukemia",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 137
              }
            },
            "id": 487,
            "cause": "B.1.28",
            "name": "Leukemia",
            "medium_name": "Leukemia",
            "short_name": "Leukemia",
            "most_detailed": 0,
            "male": 1,
            "female": 1,
            "sort_order": 132
          },
          "Other neoplasms": {
            "children": {
              "Myelodysplastic, myeloproliferative, and other hematopoietic neoplasms": {
                "children": {},
                "id": 964,
                "cause": "B.1.30.1",
                "name": "Myelodysplastic, myeloproliferative, and other hematopoietic neoplasms",
                "medium_name": "MDS, MPN, & hematop",
                "short_name": "MDS+MPN",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 140
              },
              "Benign and in situ intestinal neoplasms": {
                "children": {},
                "id": 965,
                "cause": "B.1.30.2",
                "name": "Benign and in situ intestinal neoplasms",
                "medium_name": "Intestinal benign",
                "short_name": "Intest NMN",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 141
              },
              "Benign and in situ cervical and uterine neoplasms": {
                "children": {},
                "id": 966,
                "cause": "B.1.30.3",
                "name": "Benign and in situ cervical and uterine neoplasms",
                "medium_name": "Cervical & uterine benign",
                "short_name": "Cervix NMN",
                "most_detailed": 1,
                "male": 0,
                "female": 1,
                "sort_order": 142
              },
              "Other benign and in situ neoplasms": {
                "children": {},
                "id": 967,
                "cause": "B.1.30.4",
                "name": "Other benign and in situ neoplasms",
                "medium_name": "Other benign",
                "short_name": "Oth NMN",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 143
              }
            },
            "id": 490,
            "cause": "B.1.30",
            "name": "Other neoplasms",
            "medium_name": "Other neoplasms",
            "short_name": "Other Neo",
            "most_detailed": 0,
            "male": 1,
            "female": 1,
            "sort_order": 139
          },
          "Other malignant neoplasms": {
            "children": {},
            "id": 1022,
            "cause": "B.1.29",
            "name": "Other malignant neoplasms",
            "medium_name": "Other malignant neoplasms",
            "short_name": "Other MN",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 138
          }
        },
        "id": 410,
        "cause": "B.1",
        "name": "Neoplasms",
        "medium_name": "Neoplasms",
        "short_name": "Neoplasms",
        "most_detailed": 0,
        "male": 1,
        "female": 1,
        "sort_order": 97
      },
      "Cardiovascular diseases": {
        "children": {
          "Rheumatic heart disease": {
            "children": {},
            "id": 492,
            "cause": "B.2.1",
            "name": "Rheumatic heart disease",
            "medium_name": "Rheumatic heart disease",
            "short_name": "RHD",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 145
          },
          "Ischemic heart disease": {
            "children": {},
            "id": 493,
            "cause": "B.2.2",
            "name": "Ischemic heart disease",
            "medium_name": "Ischemic heart disease",
            "short_name": "IHD",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 146
          },
          "Stroke": {
            "children": {
              "Ischemic stroke": {
                "children": {},
                "id": 495,
                "cause": "B.2.3.1",
                "name": "Ischemic stroke",
                "medium_name": "Ischemic stroke",
                "short_name": "Isch Stroke",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 148
              },
              "Intracerebral hemorrhage": {
                "children": {},
                "id": 496,
                "cause": "B.2.3.2",
                "name": "Intracerebral hemorrhage",
                "medium_name": "Intracerebral hem",
                "short_name": "Intrahem Stroke",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 149
              },
              "Subarachnoid hemorrhage": {
                "children": {},
                "id": 497,
                "cause": "B.2.3.3",
                "name": "Subarachnoid hemorrhage",
                "medium_name": "Subarachnoid hem",
                "short_name": "Sub Hem",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 150
              }
            },
            "id": 494,
            "cause": "B.2.3",
            "name": "Stroke",
            "medium_name": "Stroke",
            "short_name": "Stroke",
            "most_detailed": 0,
            "male": 1,
            "female": 1,
            "sort_order": 147
          },
          "Hypertensive heart disease": {
            "children": {},
            "id": 498,
            "cause": "B.2.4",
            "name": "Hypertensive heart disease",
            "medium_name": "Hypertensive heart disease",
            "short_name": "HTN HD",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 151
          },
          "Cardiomyopathy and myocarditis": {
            "children": {
              "Alcoholic cardiomyopathy": {
                "children": {},
                "id": 938,
                "cause": "B.2.6.2",
                "name": "Alcoholic cardiomyopathy",
                "medium_name": "Alcoholic cardiomyopathy",
                "short_name": "Alcohol CMP",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 158
              },
              "Myocarditis": {
                "children": {},
                "id": 942,
                "cause": "B.2.6.1",
                "name": "Myocarditis",
                "medium_name": "Myocarditis",
                "short_name": "Myocarditis",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 157
              },
              "Other cardiomyopathy": {
                "children": {},
                "id": 944,
                "cause": "B.2.6.3",
                "name": "Other cardiomyopathy",
                "medium_name": "Other cardiomyopathy",
                "short_name": "Oth CMP",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 159
              }
            },
            "id": 499,
            "cause": "B.2.6",
            "name": "Cardiomyopathy and myocarditis",
            "medium_name": "Cardiomyopathy",
            "short_name": "CMP",
            "most_detailed": 0,
            "male": 1,
            "female": 1,
            "sort_order": 156
          },
          "Atrial fibrillation and flutter": {
            "children": {},
            "id": 500,
            "cause": "B.2.8",
            "name": "Atrial fibrillation and flutter",
            "medium_name": "Atrial fibrillation",
            "short_name": "A Fib",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 160
          },
          "Aortic aneurysm": {
            "children": {},
            "id": 501,
            "cause": "B.2.9",
            "name": "Aortic aneurysm",
            "medium_name": "Aortic aneurysm",
            "short_name": "Aort An",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 161
          },
          "Peripheral artery disease": {
            "children": {},
            "id": 502,
            "cause": "B.2.10",
            "name": "Peripheral artery disease",
            "medium_name": "Peripheral artery",
            "short_name": "PAD",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 162
          },
          "Endocarditis": {
            "children": {},
            "id": 503,
            "cause": "B.2.11",
            "name": "Endocarditis",
            "medium_name": "Endocarditis",
            "short_name": "Endocar",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 163
          },
          "Non-rheumatic valvular heart disease": {
            "children": {
              "Non-rheumatic calcific aortic valve disease": {
                "children": {},
                "id": 968,
                "cause": "B.2.5.1",
                "name": "Non-rheumatic calcific aortic valve disease",
                "medium_name": "Nonrheum cal aort val",
                "short_name": "CAVD",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 153
              },
              "Non-rheumatic degenerative mitral valve disease": {
                "children": {},
                "id": 969,
                "cause": "B.2.5.2",
                "name": "Non-rheumatic degenerative mitral valve disease",
                "medium_name": "Nonrheum degen mit val",
                "short_name": "DMVD",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 154
              },
              "Other non-rheumatic valve diseases": {
                "children": {},
                "id": 970,
                "cause": "B.2.5.3",
                "name": "Other non-rheumatic valve diseases",
                "medium_name": "Other nonrheum valve",
                "short_name": "Oth Valvu",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 155
              }
            },
            "id": 504,
            "cause": "B.2.5",
            "name": "Non-rheumatic valvular heart disease",
            "medium_name": "Nonrheum valv diseases",
            "short_name": "Valvular",
            "most_detailed": 0,
            "male": 1,
            "female": 1,
            "sort_order": 152
          },
          "Other cardiovascular and circulatory diseases": {
            "children": {},
            "id": 1023,
            "cause": "B.2.12",
            "name": "Other cardiovascular and circulatory diseases",
            "medium_name": "Other cardiovascular",
            "short_name": "Oth Cardio",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 164
          }
        },
        "id": 491,
        "cause": "B.2",
        "name": "Cardiovascular diseases",
        "medium_name": "Cardiovascular diseases",
        "short_name": "CVD",
        "most_detailed": 0,
        "male": 1,
        "female": 1,
        "sort_order": 144
      },
      "Chronic respiratory diseases": {
        "children": {
          "Chronic obstructive pulmonary disease": {
            "children": {},
            "id": 509,
            "cause": "B.3.1",
            "name": "Chronic obstructive pulmonary disease",
            "medium_name": "COPD",
            "short_name": "COPD",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 166
          },
          "Pneumoconiosis": {
            "children": {
              "Silicosis": {
                "children": {},
                "id": 511,
                "cause": "B.3.2.1",
                "name": "Silicosis",
                "medium_name": "Silicosis",
                "short_name": "Silicosis",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 168
              },
              "Asbestosis": {
                "children": {},
                "id": 512,
                "cause": "B.3.2.2",
                "name": "Asbestosis",
                "medium_name": "Asbestosis",
                "short_name": "Asbestosis",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 169
              },
              "Coal workers pneumoconiosis": {
                "children": {},
                "id": 513,
                "cause": "B.3.2.3",
                "name": "Coal workers pneumoconiosis",
                "medium_name": "Coal workers",
                "short_name": "Coal W",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 170
              },
              "Other pneumoconiosis": {
                "children": {},
                "id": 514,
                "cause": "B.3.2.4",
                "name": "Other pneumoconiosis",
                "medium_name": "Other pneumoconiosis",
                "short_name": "Oth Pneum",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 171
              }
            },
            "id": 510,
            "cause": "B.3.2",
            "name": "Pneumoconiosis",
            "medium_name": "Pneumoconiosis",
            "short_name": "Pneumocon",
            "most_detailed": 0,
            "male": 1,
            "female": 1,
            "sort_order": 167
          },
          "Asthma": {
            "children": {},
            "id": 515,
            "cause": "B.3.3",
            "name": "Asthma",
            "medium_name": "Asthma",
            "short_name": "Asthma",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 172
          },
          "Interstitial lung disease and pulmonary sarcoidosis": {
            "children": {},
            "id": 516,
            "cause": "B.3.4",
            "name": "Interstitial lung disease and pulmonary sarcoidosis",
            "medium_name": "Interstitial lung disease",
            "short_name": "ILD",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 173
          },
          "Other chronic respiratory diseases": {
            "children": {},
            "id": 520,
            "cause": "B.3.5",
            "name": "Other chronic respiratory diseases",
            "medium_name": "Other chronic respiratory",
            "short_name": "Oth Resp",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 174
          }
        },
        "id": 508,
        "cause": "B.3",
        "name": "Chronic respiratory diseases",
        "medium_name": "Chronic respiratory",
        "short_name": "Chr Resp",
        "most_detailed": 0,
        "male": 1,
        "female": 1,
        "sort_order": 165
      },
      "Digestive diseases": {
        "children": {
          "Cirrhosis and other chronic liver diseases": {
            "children": {
              "Cirrhosis and other chronic liver diseases due to hepatitis B": {
                "children": {},
                "id": 522,
                "cause": "B.4.1.1",
                "name": "Cirrhosis and other chronic liver diseases due to hepatitis B",
                "medium_name": "Cirrhosis hepatitis B",
                "short_name": "Cirr HepB",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 177
              },
              "Cirrhosis and other chronic liver diseases due to hepatitis C": {
                "children": {},
                "id": 523,
                "cause": "B.4.1.2",
                "name": "Cirrhosis and other chronic liver diseases due to hepatitis C",
                "medium_name": "Cirrhosis hepatitis C",
                "short_name": "Cirr HepC",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 178
              },
              "Cirrhosis and other chronic liver diseases due to alcohol use": {
                "children": {},
                "id": 524,
                "cause": "B.4.1.3",
                "name": "Cirrhosis and other chronic liver diseases due to alcohol use",
                "medium_name": "Cirrhosis alcohol",
                "short_name": "Cirr Alc",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 179
              },
              "Cirrhosis and other chronic liver diseases due to other causes": {
                "children": {},
                "id": 525,
                "cause": "B.4.1.5",
                "name": "Cirrhosis and other chronic liver diseases due to other causes",
                "medium_name": "Cirrhosis other",
                "short_name": "Oth Cirr",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 181
              },
              "Cirrhosis and other chronic liver diseases due to NAFLD": {
                "children": {},
                "id": 971,
                "cause": "B.4.1.4",
                "name": "Cirrhosis and other chronic liver diseases due to NAFLD",
                "medium_name": "Cirrhosis and other due to NAFLD",
                "short_name": "Cirr Oth NAFLD",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 180
              }
            },
            "id": 521,
            "cause": "B.4.1",
            "name": "Cirrhosis and other chronic liver diseases",
            "medium_name": "Cirrhosis",
            "short_name": "Cirrhosis",
            "most_detailed": 0,
            "male": 1,
            "female": 1,
            "sort_order": 176
          },
          "Upper digestive system diseases": {
            "children": {
              "Peptic ulcer disease": {
                "children": {},
                "id": 527,
                "cause": "B.4.2.1",
                "name": "Peptic ulcer disease",
                "medium_name": "Peptic ulcer disease",
                "short_name": "PUD",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 183
              },
              "Gastritis and duodenitis": {
                "children": {},
                "id": 528,
                "cause": "B.4.2.2",
                "name": "Gastritis and duodenitis",
                "medium_name": "Gastritis & duodenitis",
                "short_name": "Gastritis",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 184
              },
              "Gastroesophageal reflux disease": {
                "children": {},
                "id": 536,
                "cause": "B.4.2.3",
                "name": "Gastroesophageal reflux disease",
                "medium_name": "Gastro reflux disease",
                "short_name": "GERD",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 185
              }
            },
            "id": 992,
            "cause": "B.4.2",
            "name": "Upper digestive system diseases",
            "medium_name": "Upper digest diseases",
            "short_name": "Upper Digest",
            "most_detailed": 0,
            "male": 1,
            "female": 1,
            "sort_order": 182
          },
          "Appendicitis": {
            "children": {},
            "id": 529,
            "cause": "B.4.3",
            "name": "Appendicitis",
            "medium_name": "Appendicitis",
            "short_name": "Appendicit",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 186
          },
          "Paralytic ileus and intestinal obstruction": {
            "children": {},
            "id": 530,
            "cause": "B.4.4",
            "name": "Paralytic ileus and intestinal obstruction",
            "medium_name": "Ileus & obstruction",
            "short_name": "Ileus",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 187
          },
          "Inguinal, femoral, and abdominal hernia": {
            "children": {},
            "id": 531,
            "cause": "B.4.5",
            "name": "Inguinal, femoral, and abdominal hernia",
            "medium_name": "Hernia",
            "short_name": "Hernia",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 188
          },
          "Inflammatory bowel disease": {
            "children": {},
            "id": 532,
            "cause": "B.4.6",
            "name": "Inflammatory bowel disease",
            "medium_name": "Inflammatory bowel",
            "short_name": "IBD",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 189
          },
          "Vascular intestinal disorders": {
            "children": {},
            "id": 533,
            "cause": "B.4.7",
            "name": "Vascular intestinal disorders",
            "medium_name": "Vascular intestinal",
            "short_name": "Vasc Intest",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 190
          },
          "Gallbladder and biliary diseases": {
            "children": {},
            "id": 534,
            "cause": "B.4.8",
            "name": "Gallbladder and biliary diseases",
            "medium_name": "Gallbladder & biliary",
            "short_name": "Gall Bile",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 191
          },
          "Pancreatitis": {
            "children": {},
            "id": 535,
            "cause": "B.4.9",
            "name": "Pancreatitis",
            "medium_name": "Pancreatitis",
            "short_name": "Pancreatit",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 192
          },
          "Other digestive diseases": {
            "children": {},
            "id": 541,
            "cause": "B.4.10",
            "name": "Other digestive diseases",
            "medium_name": "Other digestive",
            "short_name": "Oth Digest",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 193
          }
        },
        "id": 526,
        "cause": "B.4",
        "name": "Digestive diseases",
        "medium_name": "Digestive diseases",
        "short_name": "Digestive",
        "most_detailed": 0,
        "male": 1,
        "female": 1,
        "sort_order": 175
      },
      "Neurological disorders": {
        "children": {
          "Alzheimer's disease and other dementias": {
            "children": {},
            "id": 543,
            "cause": "B.5.1",
            "name": "Alzheimer's disease and other dementias",
            "medium_name": "Alzheimer's disease",
            "short_name": "Alzheimer's",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 195
          },
          "Parkinson's disease": {
            "children": {},
            "id": 544,
            "cause": "B.5.2",
            "name": "Parkinson's disease",
            "medium_name": "Parkinson's disease",
            "short_name": "Parkinson's",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 196
          },
          "Idiopathic epilepsy": {
            "children": {},
            "id": 545,
            "cause": "B.5.3",
            "name": "Idiopathic epilepsy",
            "medium_name": "Idiopathic epilepsy",
            "short_name": "Idiopathic epilepsy",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 197
          },
          "Multiple sclerosis": {
            "children": {},
            "id": 546,
            "cause": "B.5.4",
            "name": "Multiple sclerosis",
            "medium_name": "Multiple sclerosis",
            "short_name": "MS",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 198
          },
          "Headache disorders": {
            "children": {
              "Migraine": {
                "children": {},
                "id": 547,
                "cause": "B.5.6.1",
                "name": "Migraine",
                "medium_name": "Migraine",
                "short_name": "Migraine",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 201
              },
              "Tension-type headache": {
                "children": {},
                "id": 548,
                "cause": "B.5.6.2",
                "name": "Tension-type headache",
                "medium_name": "Tension headache",
                "short_name": "Tens Head",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 202
              }
            },
            "id": 972,
            "cause": "B.5.6",
            "name": "Headache disorders",
            "medium_name": "Headache disorders",
            "short_name": "Headaches",
            "most_detailed": 0,
            "male": 1,
            "female": 1,
            "sort_order": 200
          },
          "Motor neuron disease": {
            "children": {},
            "id": 554,
            "cause": "B.5.5",
            "name": "Motor neuron disease",
            "medium_name": "Motor neuron disease",
            "short_name": "ALS",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 199
          },
          "Other neurological disorders": {
            "children": {},
            "id": 557,
            "cause": "B.5.7",
            "name": "Other neurological disorders",
            "medium_name": "Other neurological",
            "short_name": "Oth Neuro",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 203
          }
        },
        "id": 542,
        "cause": "B.5",
        "name": "Neurological disorders",
        "medium_name": "Neurological disorders",
        "short_name": "Neuro",
        "most_detailed": 0,
        "male": 1,
        "female": 1,
        "sort_order": 194
      },
      "Mental disorders": {
        "children": {
          "Schizophrenia": {
            "children": {},
            "id": 559,
            "cause": "B.6.1",
            "name": "Schizophrenia",
            "medium_name": "Schizophrenia",
            "short_name": "Schiz",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 205
          },
          "Depressive disorders": {
            "children": {
              "Major depressive disorder": {
                "children": {},
                "id": 568,
                "cause": "B.6.2.1",
                "name": "Major depressive disorder",
                "medium_name": "Major depression",
                "short_name": "MDD",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 207
              },
              "Dysthymia": {
                "children": {},
                "id": 569,
                "cause": "B.6.2.2",
                "name": "Dysthymia",
                "medium_name": "Dysthymia",
                "short_name": "Dysthymia",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 208
              }
            },
            "id": 567,
            "cause": "B.6.2",
            "name": "Depressive disorders",
            "medium_name": "Depressive disorders",
            "short_name": "Depression",
            "most_detailed": 0,
            "male": 1,
            "female": 1,
            "sort_order": 206
          },
          "Bipolar disorder": {
            "children": {},
            "id": 570,
            "cause": "B.6.3",
            "name": "Bipolar disorder",
            "medium_name": "Bipolar disorder",
            "short_name": "Bipolar",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 209
          },
          "Anxiety disorders": {
            "children": {},
            "id": 571,
            "cause": "B.6.4",
            "name": "Anxiety disorders",
            "medium_name": "Anxiety disorders",
            "short_name": "Anxiety",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 210
          },
          "Eating disorders": {
            "children": {
              "Anorexia nervosa": {
                "children": {},
                "id": 573,
                "cause": "B.6.5.1",
                "name": "Anorexia nervosa",
                "medium_name": "Anorexia nervosa",
                "short_name": "Anorexia",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 212
              },
              "Bulimia nervosa": {
                "children": {},
                "id": 574,
                "cause": "B.6.5.2",
                "name": "Bulimia nervosa",
                "medium_name": "Bulimia nervosa",
                "short_name": "Bulimia",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 213
              }
            },
            "id": 572,
            "cause": "B.6.5",
            "name": "Eating disorders",
            "medium_name": "Eating disorders",
            "short_name": "Eating",
            "most_detailed": 0,
            "male": 1,
            "female": 1,
            "sort_order": 211
          },
          "Autism spectrum disorders": {
            "children": {},
            "id": 575,
            "cause": "B.6.6",
            "name": "Autism spectrum disorders",
            "medium_name": "Autism spectrum",
            "short_name": "ASD",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 214
          },
          "Attention-deficit/hyperactivity disorder": {
            "children": {},
            "id": 578,
            "cause": "B.6.7",
            "name": "Attention-deficit/hyperactivity disorder",
            "medium_name": "ADHD",
            "short_name": "ADHD",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 215
          },
          "Conduct disorder": {
            "children": {},
            "id": 579,
            "cause": "B.6.8",
            "name": "Conduct disorder",
            "medium_name": "Conduct disorder",
            "short_name": "Conduct",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 216
          },
          "Idiopathic developmental intellectual disability": {
            "children": {},
            "id": 582,
            "cause": "B.6.9",
            "name": "Idiopathic developmental intellectual disability",
            "medium_name": "Intellectual disability",
            "short_name": "ID",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 217
          },
          "Other mental disorders": {
            "children": {},
            "id": 585,
            "cause": "B.6.10",
            "name": "Other mental disorders",
            "medium_name": "Other mental disorders",
            "short_name": "Oth Ment",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 218
          }
        },
        "id": 558,
        "cause": "B.6",
        "name": "Mental disorders",
        "medium_name": "Mental disorders",
        "short_name": "Mental",
        "most_detailed": 0,
        "male": 1,
        "female": 1,
        "sort_order": 204
      },
      "Substance use disorders": {
        "children": {
          "Alcohol use disorders": {
            "children": {},
            "id": 560,
            "cause": "B.7.1",
            "name": "Alcohol use disorders",
            "medium_name": "Alcohol use disorders",
            "short_name": "Alcohol",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 220
          },
          "Drug use disorders": {
            "children": {
              "Opioid use disorders": {
                "children": {},
                "id": 562,
                "cause": "B.7.2.1",
                "name": "Opioid use disorders",
                "medium_name": "Opioid use disorders",
                "short_name": "Opioids",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 222
              },
              "Cocaine use disorders": {
                "children": {},
                "id": 563,
                "cause": "B.7.2.2",
                "name": "Cocaine use disorders",
                "medium_name": "Cocaine use disorders",
                "short_name": "Cocaine",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 223
              },
              "Amphetamine use disorders": {
                "children": {},
                "id": 564,
                "cause": "B.7.2.3",
                "name": "Amphetamine use disorders",
                "medium_name": "Amphetamine use disorders",
                "short_name": "Amphet",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 224
              },
              "Cannabis use disorders": {
                "children": {},
                "id": 565,
                "cause": "B.7.2.4",
                "name": "Cannabis use disorders",
                "medium_name": "Cannabis use disorders",
                "short_name": "Cannabis",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 225
              },
              "Other drug use disorders": {
                "children": {},
                "id": 566,
                "cause": "B.7.2.5",
                "name": "Other drug use disorders",
                "medium_name": "Other drug use disorders",
                "short_name": "Oth Drug",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 226
              }
            },
            "id": 561,
            "cause": "B.7.2",
            "name": "Drug use disorders",
            "medium_name": "Drug use disorders",
            "short_name": "Drugs",
            "most_detailed": 0,
            "male": 1,
            "female": 1,
            "sort_order": 221
          }
        },
        "id": 973,
        "cause": "B.7",
        "name": "Substance use disorders",
        "medium_name": "Substance use",
        "short_name": "Subs Use",
        "most_detailed": 0,
        "male": 1,
        "female": 1,
        "sort_order": 219
      },
      "Diabetes and kidney diseases": {
        "children": {
          "Diabetes mellitus": {
            "children": {
              "Diabetes mellitus type 1": {
                "children": {},
                "id": 975,
                "cause": "B.8.1.1",
                "name": "Diabetes mellitus type 1",
                "medium_name": "Diabetes type 1",
                "short_name": "Diabetes 1",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 229
              },
              "Diabetes mellitus type 2": {
                "children": {},
                "id": 976,
                "cause": "B.8.1.2",
                "name": "Diabetes mellitus type 2",
                "medium_name": "Diabetes type 2",
                "short_name": "Diabetes 2",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 230
              }
            },
            "id": 587,
            "cause": "B.8.1",
            "name": "Diabetes mellitus",
            "medium_name": "Diabetes",
            "short_name": "Diabetes",
            "most_detailed": 0,
            "male": 1,
            "female": 1,
            "sort_order": 228
          },
          "Acute glomerulonephritis": {
            "children": {},
            "id": 588,
            "cause": "B.8.3",
            "name": "Acute glomerulonephritis",
            "medium_name": "Acute glomerulonephritis",
            "short_name": "AGN",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 237
          },
          "Chronic kidney disease": {
            "children": {
              "Chronic kidney disease due to hypertension": {
                "children": {},
                "id": 591,
                "cause": "B.8.2.3",
                "name": "Chronic kidney disease due to hypertension",
                "medium_name": "Hypertensive CKD",
                "short_name": "HTN CKD",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 234
              },
              "Chronic kidney disease due to glomerulonephritis": {
                "children": {},
                "id": 592,
                "cause": "B.8.2.4",
                "name": "Chronic kidney disease due to glomerulonephritis",
                "medium_name": "Glomerulonephritis CKD",
                "short_name": "GN CKD",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 235
              },
              "Chronic kidney disease due to other and unspecified causes": {
                "children": {},
                "id": 593,
                "cause": "B.8.2.5",
                "name": "Chronic kidney disease due to other and unspecified causes",
                "medium_name": "Other CKD",
                "short_name": "Oth CKD",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 236
              },
              "Chronic kidney disease due to diabetes mellitus type 1": {
                "children": {},
                "id": 997,
                "cause": "B.8.2.1",
                "name": "Chronic kidney disease due to diabetes mellitus type 1",
                "medium_name": "CKD due to diabetes type 1",
                "short_name": "CKD Diabetes1",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 232
              },
              "Chronic kidney disease due to diabetes mellitus type 2": {
                "children": {},
                "id": 998,
                "cause": "B.8.2.2",
                "name": "Chronic kidney disease due to diabetes mellitus type 2",
                "medium_name": "CKD due to diabetes type 2",
                "short_name": "CKD Diabetes2",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 233
              }
            },
            "id": 589,
            "cause": "B.8.2",
            "name": "Chronic kidney disease",
            "medium_name": "Chronic kidney disease",
            "short_name": "CKD",
            "most_detailed": 0,
            "male": 1,
            "female": 1,
            "sort_order": 231
          }
        },
        "id": 974,
        "cause": "B.8",
        "name": "Diabetes and kidney diseases",
        "medium_name": "Diabetes & CKD",
        "short_name": "Diabetes+CKD",
        "most_detailed": 0,
        "male": 1,
        "female": 1,
        "sort_order": 227
      },
      "Other non-communicable diseases": {
        "children": {
          "Urinary diseases and male infertility": {
            "children": {
              "Urinary tract infections and interstitial nephritis": {
                "children": {},
                "id": 595,
                "cause": "B.12.2.1",
                "name": "Urinary tract infections and interstitial nephritis",
                "medium_name": "Urinary tract infections and interstitial nephritis",
                "short_name": "UTI and interstitial nephritis",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 291
              },
              "Urolithiasis": {
                "children": {},
                "id": 596,
                "cause": "B.12.2.2",
                "name": "Urolithiasis",
                "medium_name": "Urolithiasis",
                "short_name": "Urolith",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 292
              },
              "Benign prostatic hyperplasia": {
                "children": {},
                "id": 597,
                "cause": "B.12.2.3",
                "name": "Benign prostatic hyperplasia",
                "medium_name": "BPH",
                "short_name": "BPH",
                "most_detailed": 1,
                "male": 1,
                "female": 0,
                "sort_order": 293
              },
              "Male infertility": {
                "children": {},
                "id": 598,
                "cause": "B.12.2.4",
                "name": "Male infertility",
                "medium_name": "Male infertility",
                "short_name": "Infert M",
                "most_detailed": 1,
                "male": 1,
                "female": 0,
                "sort_order": 294
              },
              "Other urinary diseases": {
                "children": {},
                "id": 602,
                "cause": "B.12.2.5",
                "name": "Other urinary diseases",
                "medium_name": "Other urinary diseases",
                "short_name": "Oth Urin",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 295
              }
            },
            "id": 594,
            "cause": "B.12.2",
            "name": "Urinary diseases and male infertility",
            "medium_name": "Urinary diseases",
            "short_name": "Urinary",
            "most_detailed": 0,
            "male": 1,
            "female": 1,
            "sort_order": 290
          },
          "Gynecological diseases": {
            "children": {
              "Uterine fibroids": {
                "children": {},
                "id": 604,
                "cause": "B.12.3.1",
                "name": "Uterine fibroids",
                "medium_name": "Uterine fibroids",
                "short_name": "Fibroids",
                "most_detailed": 1,
                "male": 0,
                "female": 1,
                "sort_order": 297
              },
              "Polycystic ovarian syndrome": {
                "children": {},
                "id": 605,
                "cause": "B.12.3.2",
                "name": "Polycystic ovarian syndrome",
                "medium_name": "Polycystic ovary syndrome",
                "short_name": "PCOS",
                "most_detailed": 1,
                "male": 0,
                "female": 1,
                "sort_order": 298
              },
              "Female infertility": {
                "children": {},
                "id": 606,
                "cause": "B.12.3.3",
                "name": "Female infertility",
                "medium_name": "Female infertility",
                "short_name": "Infert F",
                "most_detailed": 1,
                "male": 0,
                "female": 1,
                "sort_order": 299
              },
              "Endometriosis": {
                "children": {},
                "id": 607,
                "cause": "B.12.3.4",
                "name": "Endometriosis",
                "medium_name": "Endometriosis",
                "short_name": "Endomet",
                "most_detailed": 1,
                "male": 0,
                "female": 1,
                "sort_order": 300
              },
              "Genital prolapse": {
                "children": {},
                "id": 608,
                "cause": "B.12.3.5",
                "name": "Genital prolapse",
                "medium_name": "Genital prolapse",
                "short_name": "Prolapse",
                "most_detailed": 1,
                "male": 0,
                "female": 1,
                "sort_order": 301
              },
              "Premenstrual syndrome": {
                "children": {},
                "id": 609,
                "cause": "B.12.3.6",
                "name": "Premenstrual syndrome",
                "medium_name": "Premenstrual syndrome",
                "short_name": "PMS",
                "most_detailed": 1,
                "male": 0,
                "female": 1,
                "sort_order": 302
              },
              "Other gynecological diseases": {
                "children": {},
                "id": 612,
                "cause": "B.12.3.7",
                "name": "Other gynecological diseases",
                "medium_name": "Other gynecological",
                "short_name": "Oth Gyne",
                "most_detailed": 1,
                "male": 0,
                "female": 1,
                "sort_order": 303
              }
            },
            "id": 603,
            "cause": "B.12.3",
            "name": "Gynecological diseases",
            "medium_name": "Gynecological diseases",
            "short_name": "Gyne",
            "most_detailed": 0,
            "male": 0,
            "female": 1,
            "sort_order": 296
          },
          "Hemoglobinopathies and hemolytic anemias": {
            "children": {
              "Thalassemias": {
                "children": {},
                "id": 614,
                "cause": "B.12.4.1",
                "name": "Thalassemias",
                "medium_name": "Thalassemia",
                "short_name": "Thalass",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 305
              },
              "Sickle cell disorders": {
                "children": {},
                "id": 615,
                "cause": "B.12.4.3",
                "name": "Sickle cell disorders",
                "medium_name": "Sickle cell",
                "short_name": "Sickle",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 307
              },
              "G6PD deficiency": {
                "children": {},
                "id": 616,
                "cause": "B.12.4.5",
                "name": "G6PD deficiency",
                "medium_name": "G6PD deficiency",
                "short_name": "G6PD",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 309
              },
              "Other hemoglobinopathies and hemolytic anemias": {
                "children": {},
                "id": 618,
                "cause": "B.12.4.7",
                "name": "Other hemoglobinopathies and hemolytic anemias",
                "medium_name": "Other hemoglobinopathies",
                "short_name": "Oth Hem",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 311
              },
              "Thalassemias trait": {
                "children": {},
                "id": 837,
                "cause": "B.12.4.2",
                "name": "Thalassemias trait",
                "medium_name": "Thalassemia trait",
                "short_name": "Thalass Trait",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 306
              },
              "Sickle cell trait": {
                "children": {},
                "id": 838,
                "cause": "B.12.4.4",
                "name": "Sickle cell trait",
                "medium_name": "Sickle cell trait",
                "short_name": "Sickle Trait",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 308
              },
              "G6PD trait": {
                "children": {},
                "id": 839,
                "cause": "B.12.4.6",
                "name": "G6PD trait",
                "medium_name": "G6PD trait",
                "short_name": "G6PD Trait",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 310
              }
            },
            "id": 613,
            "cause": "B.12.4",
            "name": "Hemoglobinopathies and hemolytic anemias",
            "medium_name": "Hemoglobinopathies",
            "short_name": "Hemog",
            "most_detailed": 0,
            "male": 1,
            "female": 1,
            "sort_order": 304
          },
          "Endocrine, metabolic, blood, and immune disorders": {
            "children": {},
            "id": 619,
            "cause": "B.12.5",
            "name": "Endocrine, metabolic, blood, and immune disorders",
            "medium_name": "Endo/metab/blood/immune",
            "short_name": "Endocrine",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 312
          },
          "Congenital birth defects": {
            "children": {
              "Neural tube defects": {
                "children": {},
                "id": 642,
                "cause": "B.12.1.1",
                "name": "Neural tube defects",
                "medium_name": "Neural tube defects",
                "short_name": "Neur Tube",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 279
              },
              "Congenital heart anomalies": {
                "children": {},
                "id": 643,
                "cause": "B.12.1.2",
                "name": "Congenital heart anomalies",
                "medium_name": "Congenital heart",
                "short_name": "Cong Heart",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 280
              },
              "Orofacial clefts": {
                "children": {},
                "id": 644,
                "cause": "B.12.1.3",
                "name": "Orofacial clefts",
                "medium_name": "Orofacial clefts",
                "short_name": "Cleft",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 281
              },
              "Down syndrome": {
                "children": {},
                "id": 645,
                "cause": "B.12.1.4",
                "name": "Down syndrome",
                "medium_name": "Down syndrome",
                "short_name": "Down",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 282
              },
              "Turner syndrome": {
                "children": {},
                "id": 646,
                "cause": "B.12.1.5",
                "name": "Turner syndrome",
                "medium_name": "Turner syndrome",
                "short_name": "Turner",
                "most_detailed": 1,
                "male": 0,
                "female": 1,
                "sort_order": 283
              },
              "Klinefelter syndrome": {
                "children": {},
                "id": 647,
                "cause": "B.12.1.6",
                "name": "Klinefelter syndrome",
                "medium_name": "Klinefelter syndrome",
                "short_name": "Klinefelter",
                "most_detailed": 1,
                "male": 1,
                "female": 0,
                "sort_order": 284
              },
              "Other chromosomal abnormalities": {
                "children": {},
                "id": 648,
                "cause": "B.12.1.7",
                "name": "Other chromosomal abnormalities",
                "medium_name": "Chromosomal unbalanced",
                "short_name": "Chrom Unb",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 285
              },
              "Congenital musculoskeletal and limb anomalies": {
                "children": {},
                "id": 649,
                "cause": "B.12.1.8",
                "name": "Congenital musculoskeletal and limb anomalies",
                "medium_name": "Congenital musculoskeletal",
                "short_name": "Cong MSK",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 286
              },
              "Urogenital congenital anomalies": {
                "children": {},
                "id": 650,
                "cause": "B.12.1.9",
                "name": "Urogenital congenital anomalies",
                "medium_name": "Urogenital congenital",
                "short_name": "Cong Urogen",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 287
              },
              "Digestive congenital anomalies": {
                "children": {},
                "id": 651,
                "cause": "B.12.1.10",
                "name": "Digestive congenital anomalies",
                "medium_name": "Digestive cong anomalies",
                "short_name": "Digest Anom",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 288
              },
              "Other congenital birth defects": {
                "children": {},
                "id": 652,
                "cause": "B.12.1.11",
                "name": "Other congenital birth defects",
                "medium_name": "Other congenital",
                "short_name": "Oth Cong",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 289
              }
            },
            "id": 641,
            "cause": "B.12.1",
            "name": "Congenital birth defects",
            "medium_name": "Congenital defects",
            "short_name": "Congenital",
            "most_detailed": 0,
            "male": 1,
            "female": 1,
            "sort_order": 278
          },
          "Oral disorders": {
            "children": {
              "Caries of deciduous teeth": {
                "children": {},
                "id": 681,
                "cause": "B.12.6.1",
                "name": "Caries of deciduous teeth",
                "medium_name": "Deciduous caries",
                "short_name": "Dec Caries",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 314
              },
              "Caries of permanent teeth": {
                "children": {},
                "id": 682,
                "cause": "B.12.6.2",
                "name": "Caries of permanent teeth",
                "medium_name": "Permanent caries",
                "short_name": "Per Caries",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 315
              },
              "Periodontal diseases": {
                "children": {},
                "id": 683,
                "cause": "B.12.6.3",
                "name": "Periodontal diseases",
                "medium_name": "Periodontal diseases",
                "short_name": "Period",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 316
              },
              "Edentulism": {
                "children": {},
                "id": 684,
                "cause": "B.12.6.4",
                "name": "Edentulism",
                "medium_name": "Edentulism",
                "short_name": "Edentul",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 317
              },
              "Other oral disorders": {
                "children": {},
                "id": 685,
                "cause": "B.12.6.5",
                "name": "Other oral disorders",
                "medium_name": "Other oral disorders",
                "short_name": "Other Oral",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 318
              }
            },
            "id": 680,
            "cause": "B.12.6",
            "name": "Oral disorders",
            "medium_name": "Oral disorders",
            "short_name": "Oral",
            "most_detailed": 0,
            "male": 1,
            "female": 1,
            "sort_order": 313
          },
          "Sudden infant death syndrome": {
            "children": {},
            "id": 686,
            "cause": "B.12.7",
            "name": "Sudden infant death syndrome",
            "medium_name": "SIDS",
            "short_name": "SIDS",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 319
          }
        },
        "id": 640,
        "cause": "B.12",
        "name": "Other non-communicable diseases",
        "medium_name": "Other non-communicable",
        "short_name": "Oth NCD",
        "most_detailed": 0,
        "male": 1,
        "female": 1,
        "sort_order": 277
      },
      "Musculoskeletal disorders": {
        "children": {
          "Rheumatoid arthritis": {
            "children": {},
            "id": 627,
            "cause": "B.11.1",
            "name": "Rheumatoid arthritis",
            "medium_name": "Rheumatoid arthritis",
            "short_name": "Rheu Arth",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 267
          },
          "Osteoarthritis": {
            "children": {
              "Osteoarthritis hip": {
                "children": {},
                "id": 1014,
                "cause": "B.11.2.1",
                "name": "Osteoarthritis hip",
                "medium_name": "Osteoarthritis hip",
                "short_name": "Osteoarth Hip",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 269
              },
              "Osteoarthritis knee": {
                "children": {},
                "id": 1015,
                "cause": "B.11.2.2",
                "name": "Osteoarthritis knee",
                "medium_name": "Osteoarthritis knee",
                "short_name": "Osteoarth Knee",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 270
              },
              "Osteoarthritis hand": {
                "children": {},
                "id": 1016,
                "cause": "B.11.2.3",
                "name": "Osteoarthritis hand",
                "medium_name": "Osteoarthritis hand",
                "short_name": "Osteoarth Hand",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 271
              },
              "Osteoarthritis other": {
                "children": {},
                "id": 1017,
                "cause": "B.11.2.4",
                "name": "Osteoarthritis other",
                "medium_name": "Osteoarthritis other",
                "short_name": "Osteoarth Oth",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 272
              }
            },
            "id": 628,
            "cause": "B.11.2",
            "name": "Osteoarthritis",
            "medium_name": "Osteoarthritis",
            "short_name": "Osteoarth",
            "most_detailed": 0,
            "male": 1,
            "female": 1,
            "sort_order": 268
          },
          "Low back pain": {
            "children": {},
            "id": 630,
            "cause": "B.11.3",
            "name": "Low back pain",
            "medium_name": "Low back pain",
            "short_name": "Back Pain",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 273
          },
          "Neck pain": {
            "children": {},
            "id": 631,
            "cause": "B.11.4",
            "name": "Neck pain",
            "medium_name": "Neck pain",
            "short_name": "Neck Pain",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 274
          },
          "Gout": {
            "children": {},
            "id": 632,
            "cause": "B.11.5",
            "name": "Gout",
            "medium_name": "Gout",
            "short_name": "Gout",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 275
          },
          "Other musculoskeletal disorders": {
            "children": {},
            "id": 639,
            "cause": "B.11.6",
            "name": "Other musculoskeletal disorders",
            "medium_name": "Other musculoskeletal",
            "short_name": "Oth MSK",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 276
          }
        },
        "id": 626,
        "cause": "B.11",
        "name": "Musculoskeletal disorders",
        "medium_name": "Musculoskeletal disorders",
        "short_name": "MSK",
        "most_detailed": 0,
        "male": 1,
        "female": 1,
        "sort_order": 266
      },
      "Skin and subcutaneous diseases": {
        "children": {
          "Dermatitis": {
            "children": {
              "Atopic dermatitis": {
                "children": {},
                "id": 977,
                "cause": "B.9.1.1",
                "name": "Atopic dermatitis",
                "medium_name": "Atopic derm",
                "short_name": "Atopic Derm",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 240
              },
              "Contact dermatitis": {
                "children": {},
                "id": 978,
                "cause": "B.9.1.2",
                "name": "Contact dermatitis",
                "medium_name": "Contact derm",
                "short_name": "Contact Derm",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 241
              },
              "Seborrhoeic dermatitis": {
                "children": {},
                "id": 979,
                "cause": "B.9.1.3",
                "name": "Seborrhoeic dermatitis",
                "medium_name": "Seborrhoeic derm",
                "short_name": "Seborr Derm",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 242
              }
            },
            "id": 654,
            "cause": "B.9.1",
            "name": "Dermatitis",
            "medium_name": "Dermatitis",
            "short_name": "Dermatitis",
            "most_detailed": 0,
            "male": 1,
            "female": 1,
            "sort_order": 239
          },
          "Psoriasis": {
            "children": {},
            "id": 655,
            "cause": "B.9.2",
            "name": "Psoriasis",
            "medium_name": "Psoriasis",
            "short_name": "Psoriasis",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 243
          },
          "Bacterial skin diseases": {
            "children": {
              "Cellulitis": {
                "children": {},
                "id": 656,
                "cause": "B.9.3.1",
                "name": "Cellulitis",
                "medium_name": "Cellulitis",
                "short_name": "Cellulitis",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 245
              },
              "Pyoderma": {
                "children": {},
                "id": 657,
                "cause": "B.9.3.2",
                "name": "Pyoderma",
                "medium_name": "Pyoderma",
                "short_name": "Pyoderma",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 246
              }
            },
            "id": 980,
            "cause": "B.9.3",
            "name": "Bacterial skin diseases",
            "medium_name": "Bacterial skin",
            "short_name": "Bac Skin",
            "most_detailed": 0,
            "male": 1,
            "female": 1,
            "sort_order": 244
          },
          "Scabies": {
            "children": {},
            "id": 658,
            "cause": "B.9.4",
            "name": "Scabies",
            "medium_name": "Scabies",
            "short_name": "Scabies",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 247
          },
          "Fungal skin diseases": {
            "children": {},
            "id": 659,
            "cause": "B.9.5",
            "name": "Fungal skin diseases",
            "medium_name": "Fungal skin diseases",
            "short_name": "Skin Fung",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 248
          },
          "Viral skin diseases": {
            "children": {},
            "id": 660,
            "cause": "B.9.6",
            "name": "Viral skin diseases",
            "medium_name": "Viral skin diseases",
            "short_name": "Skin Viral",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 249
          },
          "Acne vulgaris": {
            "children": {},
            "id": 661,
            "cause": "B.9.7",
            "name": "Acne vulgaris",
            "medium_name": "Acne vulgaris",
            "short_name": "Acne",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 250
          },
          "Alopecia areata": {
            "children": {},
            "id": 662,
            "cause": "B.9.8",
            "name": "Alopecia areata",
            "medium_name": "Alopecia areata",
            "short_name": "Alopecia",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 251
          },
          "Pruritus": {
            "children": {},
            "id": 663,
            "cause": "B.9.9",
            "name": "Pruritus",
            "medium_name": "Pruritus",
            "short_name": "Pruritus",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 252
          },
          "Urticaria": {
            "children": {},
            "id": 664,
            "cause": "B.9.10",
            "name": "Urticaria",
            "medium_name": "Urticaria",
            "short_name": "Urticaria",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 253
          },
          "Decubitus ulcer": {
            "children": {},
            "id": 665,
            "cause": "B.9.11",
            "name": "Decubitus ulcer",
            "medium_name": "Decubitus ulcer",
            "short_name": "Decubitus",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 254
          },
          "Other skin and subcutaneous diseases": {
            "children": {},
            "id": 668,
            "cause": "B.9.12",
            "name": "Other skin and subcutaneous diseases",
            "medium_name": "Other skin diseases",
            "short_name": "Oth Skin",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 255
          }
        },
        "id": 653,
        "cause": "B.9",
        "name": "Skin and subcutaneous diseases",
        "medium_name": "Skin diseases",
        "short_name": "Skin",
        "most_detailed": 0,
        "male": 1,
        "female": 1,
        "sort_order": 238
      },
      "Sense organ diseases": {
        "children": {
          "Blindness and vision loss": {
            "children": {
              "Glaucoma": {
                "children": {},
                "id": 670,
                "cause": "B.10.1.1",
                "name": "Glaucoma",
                "medium_name": "Glaucoma",
                "short_name": "Glaucoma",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 258
              },
              "Cataract": {
                "children": {},
                "id": 671,
                "cause": "B.10.1.2",
                "name": "Cataract",
                "medium_name": "Cataract",
                "short_name": "Cataract",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 259
              },
              "Age-related macular degeneration": {
                "children": {},
                "id": 672,
                "cause": "B.10.1.3",
                "name": "Age-related macular degeneration",
                "medium_name": "Age-related macular degeneration",
                "short_name": "Macular",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 260
              },
              "Other vision loss": {
                "children": {},
                "id": 675,
                "cause": "B.10.1.6",
                "name": "Other vision loss",
                "medium_name": "Other vision loss",
                "short_name": "Oth Vision",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 263
              },
              "Refraction disorders": {
                "children": {},
                "id": 999,
                "cause": "B.10.1.4",
                "name": "Refraction disorders",
                "medium_name": "Refraction disorders",
                "short_name": "Refraction",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 261
              },
              "Near vision loss": {
                "children": {},
                "id": 1000,
                "cause": "B.10.1.5",
                "name": "Near vision loss",
                "medium_name": "Near vision loss",
                "short_name": "Near vision",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 262
              }
            },
            "id": 981,
            "cause": "B.10.1",
            "name": "Blindness and vision loss",
            "medium_name": "Blindness and vision loss",
            "short_name": "Blindness",
            "most_detailed": 0,
            "male": 1,
            "female": 1,
            "sort_order": 257
          },
          "Age-related and other hearing loss": {
            "children": {},
            "id": 674,
            "cause": "B.10.2",
            "name": "Age-related and other hearing loss",
            "medium_name": "Age-related hearing loss",
            "short_name": "Hearing",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 264
          },
          "Other sense organ diseases": {
            "children": {},
            "id": 679,
            "cause": "B.10.3",
            "name": "Other sense organ diseases",
            "medium_name": "Other sense organ",
            "short_name": "Oth Sense",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 265
          }
        },
        "id": 669,
        "cause": "B.10",
        "name": "Sense organ diseases",
        "medium_name": "Sense organ diseases",
        "short_name": "Sense",
        "most_detailed": 0,
        "male": 1,
        "female": 1,
        "sort_order": 256
      }
    },
    "id": 409,
    "cause": "B",
    "name": "Non-communicable diseases",
    "medium_name": "Non-communicable",
    "short_name": "NCD",
    "most_detailed": 0,
    "male": 1,
    "female": 1,
    "sort_order": 96
  },
  "Injuries": {
    "children": {
      "Transport injuries": {
        "children": {
          "Road injuries": {
            "children": {
              "Pedestrian road injuries": {
                "children": {},
                "id": 690,
                "cause": "C.1.1.1",
                "name": "Pedestrian road injuries",
                "medium_name": "Pedestrian road inj",
                "short_name": "Pedest",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 323
              },
              "Cyclist road injuries": {
                "children": {},
                "id": 691,
                "cause": "C.1.1.2",
                "name": "Cyclist road injuries",
                "medium_name": "Cyclist road inj",
                "short_name": "Cyclist",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 324
              },
              "Motorcyclist road injuries": {
                "children": {},
                "id": 692,
                "cause": "C.1.1.3",
                "name": "Motorcyclist road injuries",
                "medium_name": "Motorcyclist road inj",
                "short_name": "Mot Cyc",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 325
              },
              "Motor vehicle road injuries": {
                "children": {},
                "id": 693,
                "cause": "C.1.1.4",
                "name": "Motor vehicle road injuries",
                "medium_name": "Motor vehicle road inj",
                "short_name": "Mot Veh",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 326
              },
              "Other road injuries": {
                "children": {},
                "id": 694,
                "cause": "C.1.1.5",
                "name": "Other road injuries",
                "medium_name": "Other road inj",
                "short_name": "Oth Road",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 327
              }
            },
            "id": 689,
            "cause": "C.1.1",
            "name": "Road injuries",
            "medium_name": "Road injuries",
            "short_name": "Road Inj",
            "most_detailed": 0,
            "male": 1,
            "female": 1,
            "sort_order": 322
          },
          "Other transport injuries": {
            "children": {},
            "id": 695,
            "cause": "C.1.2",
            "name": "Other transport injuries",
            "medium_name": "Other transport inj",
            "short_name": "Oth Trans",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 328
          }
        },
        "id": 688,
        "cause": "C.1",
        "name": "Transport injuries",
        "medium_name": "Transport injuries",
        "short_name": "Trans Inj",
        "most_detailed": 0,
        "male": 1,
        "female": 1,
        "sort_order": 321
      },
      "Unintentional injuries": {
        "children": {
          "Falls": {
            "children": {},
            "id": 697,
            "cause": "C.2.1",
            "name": "Falls",
            "medium_name": "Falls",
            "short_name": "Falls",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 330
          },
          "Drowning": {
            "children": {},
            "id": 698,
            "cause": "C.2.2",
            "name": "Drowning",
            "medium_name": "Drowning",
            "short_name": "Drown",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 331
          },
          "Fire, heat, and hot substances": {
            "children": {},
            "id": 699,
            "cause": "C.2.3",
            "name": "Fire, heat, and hot substances",
            "medium_name": "Fire & heat",
            "short_name": "Fire",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 332
          },
          "Poisonings": {
            "children": {
              "Poisoning by carbon monoxide": {
                "children": {},
                "id": 701,
                "cause": "C.2.4.1",
                "name": "Poisoning by carbon monoxide",
                "medium_name": "Poisoning by carbon monoxide",
                "short_name": "Inj Pois CO",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 334
              },
              "Poisoning by other means": {
                "children": {},
                "id": 703,
                "cause": "C.2.4.2",
                "name": "Poisoning by other means",
                "medium_name": "Poisoning by other means",
                "short_name": "Inj Pois Oth",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 335
              }
            },
            "id": 700,
            "cause": "C.2.4",
            "name": "Poisonings",
            "medium_name": "Poisonings",
            "short_name": "Poison",
            "most_detailed": 0,
            "male": 1,
            "female": 1,
            "sort_order": 333
          },
          "Exposure to mechanical forces": {
            "children": {
              "Unintentional firearm injuries": {
                "children": {},
                "id": 705,
                "cause": "C.2.5.1",
                "name": "Unintentional firearm injuries",
                "medium_name": "Unintentional firearm",
                "short_name": "Mech Gun",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 337
              },
              "Other exposure to mechanical forces": {
                "children": {},
                "id": 707,
                "cause": "C.2.5.2",
                "name": "Other exposure to mechanical forces",
                "medium_name": "Other mechanical forces",
                "short_name": "Oth Mech",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 338
              }
            },
            "id": 704,
            "cause": "C.2.5",
            "name": "Exposure to mechanical forces",
            "medium_name": "Mechanical forces",
            "short_name": "Mech",
            "most_detailed": 0,
            "male": 1,
            "female": 1,
            "sort_order": 336
          },
          "Adverse effects of medical treatment": {
            "children": {},
            "id": 708,
            "cause": "C.2.6",
            "name": "Adverse effects of medical treatment",
            "medium_name": "Adverse medical treatment",
            "short_name": "Med Treat",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 339
          },
          "Animal contact": {
            "children": {
              "Venomous animal contact": {
                "children": {},
                "id": 710,
                "cause": "C.2.7.1",
                "name": "Venomous animal contact",
                "medium_name": "Venomous animal",
                "short_name": "Venom",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 341
              },
              "Non-venomous animal contact": {
                "children": {},
                "id": 711,
                "cause": "C.2.7.2",
                "name": "Non-venomous animal contact",
                "medium_name": "Non-venomous animal",
                "short_name": "Non Ven",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 342
              }
            },
            "id": 709,
            "cause": "C.2.7",
            "name": "Animal contact",
            "medium_name": "Animal contact",
            "short_name": "Animal",
            "most_detailed": 0,
            "male": 1,
            "female": 1,
            "sort_order": 340
          },
          "Foreign body": {
            "children": {
              "Pulmonary aspiration and foreign body in airway": {
                "children": {},
                "id": 713,
                "cause": "C.2.8.1",
                "name": "Pulmonary aspiration and foreign body in airway",
                "medium_name": "Pulmonary aspiration",
                "short_name": "F Body Asp",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 344
              },
              "Foreign body in eyes": {
                "children": {},
                "id": 714,
                "cause": "C.2.8.2",
                "name": "Foreign body in eyes",
                "medium_name": "Foreign body in eye",
                "short_name": "F Body Eye",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 345
              },
              "Foreign body in other body part": {
                "children": {},
                "id": 715,
                "cause": "C.2.8.3",
                "name": "Foreign body in other body part",
                "medium_name": "Other foreign body",
                "short_name": "Oth F Body",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 346
              }
            },
            "id": 712,
            "cause": "C.2.8",
            "name": "Foreign body",
            "medium_name": "Foreign body",
            "short_name": "F Body",
            "most_detailed": 0,
            "male": 1,
            "female": 1,
            "sort_order": 343
          },
          "Other unintentional injuries": {
            "children": {},
            "id": 716,
            "cause": "C.2.11",
            "name": "Other unintentional injuries",
            "medium_name": "Other unintentional",
            "short_name": "Oth Unint",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 349
          },
          "Exposure to forces of nature": {
            "children": {},
            "id": 729,
            "cause": "C.2.10",
            "name": "Exposure to forces of nature",
            "medium_name": "Nature disaster",
            "short_name": "Disaster",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 348
          },
          "Environmental heat and cold exposure": {
            "children": {},
            "id": 842,
            "cause": "C.2.9",
            "name": "Environmental heat and cold exposure",
            "medium_name": "Environ heat and cold",
            "short_name": "Heat + cold",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 347
          }
        },
        "id": 696,
        "cause": "C.2",
        "name": "Unintentional injuries",
        "medium_name": "Unintentional inj",
        "short_name": "Unint Inj",
        "most_detailed": 0,
        "male": 1,
        "female": 1,
        "sort_order": 329
      },
      "Self-harm and interpersonal violence": {
        "children": {
          "Self-harm": {
            "children": {
              "Self-harm by firearm": {
                "children": {},
                "id": 721,
                "cause": "C.3.1.1",
                "name": "Self-harm by firearm",
                "medium_name": "Self-harm by firearm",
                "short_name": "Self Fire",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 352
              },
              "Self-harm by other specified means": {
                "children": {},
                "id": 723,
                "cause": "C.3.1.2",
                "name": "Self-harm by other specified means",
                "medium_name": "Self-harm other means",
                "short_name": "Self Other",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 353
              }
            },
            "id": 718,
            "cause": "C.3.1",
            "name": "Self-harm",
            "medium_name": "Self-harm",
            "short_name": "Self Harm",
            "most_detailed": 0,
            "male": 1,
            "female": 1,
            "sort_order": 351
          },
          "Interpersonal violence": {
            "children": {
              "Physical violence by firearm": {
                "children": {},
                "id": 725,
                "cause": "C.3.2.1",
                "name": "Physical violence by firearm",
                "medium_name": "Violence firearm",
                "short_name": "Viol Gun",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 355
              },
              "Physical violence by sharp object": {
                "children": {},
                "id": 726,
                "cause": "C.3.2.2",
                "name": "Physical violence by sharp object",
                "medium_name": "Violence sharp object",
                "short_name": "Viol Knife",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 356
              },
              "Physical violence by other means": {
                "children": {},
                "id": 727,
                "cause": "C.3.2.4",
                "name": "Physical violence by other means",
                "medium_name": "Violence other means",
                "short_name": "Oth Viol",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 358
              },
              "Sexual violence": {
                "children": {},
                "id": 941,
                "cause": "C.3.2.3",
                "name": "Sexual violence",
                "medium_name": "Sexual violence",
                "short_name": "Sex Viol",
                "most_detailed": 1,
                "male": 1,
                "female": 1,
                "sort_order": 357
              }
            },
            "id": 724,
            "cause": "C.3.2",
            "name": "Interpersonal violence",
            "medium_name": "Interpersonal violence",
            "short_name": "Violence",
            "most_detailed": 0,
            "male": 1,
            "female": 1,
            "sort_order": 354
          },
          "Executions and police conflict": {
            "children": {},
            "id": 854,
            "cause": "C.3.4",
            "name": "Executions and police conflict",
            "medium_name": "Execution & police",
            "short_name": "Exec & Police",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 360
          },
          "Conflict and terrorism": {
            "children": {},
            "id": 945,
            "cause": "C.3.3",
            "name": "Conflict and terrorism",
            "medium_name": "Conflict & terror",
            "short_name": "Conflict Terror",
            "most_detailed": 1,
            "male": 1,
            "female": 1,
            "sort_order": 359
          }
        },
        "id": 717,
        "cause": "C.3",
        "name": "Self-harm and interpersonal violence",
        "medium_name": "Self-harm & violence",
        "short_name": "Self-harm & IPV",
        "most_detailed": 0,
        "male": 1,
        "female": 1,
        "sort_order": 350
      }
    },
    "id": 687,
    "cause": "C",
    "name": "Injuries",
    "medium_name": "Injuries",
    "short_name": "Injuries",
    "most_detailed": 0,
    "male": 1,
    "female": 1,
    "sort_order": 320
  },
  "Total burden related to hepatitis B": {
    "children": {},
    "id": 1026,
    "cause": "E",
    "name": "Total burden related to hepatitis B",
    "medium_name": "Total burden related to hep B",
    "short_name": "Tot Hep B",
    "most_detailed": 1,
    "male": 1,
    "female": 1,
    "sort_order": 362
  },
  "Total burden related to hepatitis C": {
    "children": {},
    "id": 1027,
    "cause": "F",
    "name": "Total burden related to hepatitis C",
    "medium_name": "Total burden related to hep C",
    "short_name": "Tot Hep C",
    "most_detailed": 1,
    "male": 1,
    "female": 1,
    "sort_order": 363
  },
  "Total burden related to Non-alcoholic fatty liver disease (NAFLD)": {
    "children": {},
    "id": 1028,
    "cause": "G",
    "name": "Total burden related to Non-alcoholic fatty liver disease (NAFLD)",
    "medium_name": "Total burden related to NAFLD",
    "short_name": "Tot NAFLD",
    "most_detailed": 1,
    "male": 1,
    "female": 1,
    "sort_order": 364
  },
  "Total cancers": {
    "children": {},
    "id": 1029,
    "cause": "D",
    "name": "Total cancers",
    "medium_name": "Total cancers",
    "short_name": "Tot Cancer",
    "most_detailed": 1,
    "male": 1,
    "female": 1,
    "sort_order": 361
  }
}

class JSObjectDropdown(tk.Frame):
    def __init__(self, parent, js_obj):
        super().__init__(parent)
        self.js_obj = js_obj
        self.selection = set()
        self.dropdowns = {}
        self._create_widgets()

    def _create_widgets(self):
        for key, value in self.js_obj.items():
            # Create a label for the dropdown
            label = tk.Label(self, text=key)
            label.pack(side=tk.TOP)

            # Create a dropdown menu for the value
            dropdown = tk.OptionMenu(self, tk.StringVar(), *value.keys(), command=self._update_selection)
            dropdown.pack(side=tk.TOP)

            # Save a reference to the dropdown
            self.dropdowns[key] = dropdown

    def _update_selection(self, _):
        # Update the selection set with the current values of all dropdowns
        self.selection = set()
        for dropdown in self.dropdowns.values():
            value = dropdown.cget('text')
            if value:
                self.selection.add(value)

class App(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.dropdown = JSObjectDropdown(self, js_obj)
        self.dropdown.pack(side=tk.TOP)
        self.button = tk.Button(self, text="Select", command=self._on_select)
        self.button.pack(side=tk.TOP)
        self.selection_label = tk.Label(self, text="Selection:")
        self.selection_label.pack(side=tk.TOP)
        self.selection_var = tk.StringVar()
        self.selection_var.set("")
        self.selection_label = tk.Label(self, textvariable=self.selection_var)
        self.selection_label.pack(side=tk.TOP)

    def _on_select(self):
        # Update the selection label with the current selection set
        selection = ", ".join(self.dropdown.selection)
        self.selection_var.set(selection)

# Create the main window and run the app
root = tk.Tk()
app = App(root)
app.pack()
root.mainloop()