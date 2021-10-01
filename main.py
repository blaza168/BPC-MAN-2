import re
from functions import parse_entry

entry_stop = "\d\.[a-zA-Z]"
dataset="Zsolt Geretovszky            University of Szeged, Hungary,2,33,16.50.Giorgio Maddaluno,Ziming Zhong            none,1,56,56.00.Zhixian X Jiu            Wuhan Polytechnic University, China,2,4,2.00.Zhen Zhen Wang            Xi'an Jiaotong University, China,4,60,15.00.Zefeng Yang            Southwest Jiaotong University, China,1,8,8.00.Yuzhou Song            Tsinghua University, China,1,1,1.00.Yujie Feng            Harbin Institute of Technology, China,2,23,XI.50.Yu Ding            Nanjing University of Information Science and Technology, China,3,93,31.00.Yoshihiro Deguchi            Tokushima University, Japan,4,60,15.00.Yong-Ill Lee            Changwon National University, South Korea,3,252,84.00.Yong Feng Lu            University of Nebraska–Lincoln, United States,2,24,12.00.Ying Yin Tsui            University of Alberta, Canada,2,72,36.00.Ye-Zheng Tao            University of Wisconsin–Madison, United States,1,1,1.00.Yaoming Liu            University of Illinois at Chicago, United States,1,17,17.00.Yangmin Guo            Huazhong University of Science and Technology, China,1,15,15.00.Xuan Xiao            University of Michigan, United States,3,36,12.00.Xinwei Wang            Iowa State University, United States,1,6,6.00.Xiaona Liu            Binzhou Medical University, China,1,16,16.00.Xiaohua Tan            China Academy of Engineering Physics, China,1,0,-.Xian-Deng Hou            Sichuan University, China,4,210,52.50.Wolfgang Schade            Clausthal University of Technology, Germany,2,220,110.00.Whitney V Christian            Medtronic (United States), United States,1,26,26.00.Wenfu Wei            Southwest Jiaotong University, China,1,8,8.00.Wei Hang            Xiamen University, China,1,91,91.00.Walter Koechner            Fibertek (United States), United States,1,91,91.00.Vojtech Adam            Mendel University in Brno, Czechia,2,159,79.50.Violeta M Petrović            University of Kragujevac, Serbia,1,0,-.Vincent Motto-Ros            Institut Lumière Matière, France,7,256,36.57.Vikas Sudesh and Richard J S Morrison            none,none,1,0,0.Vı Tĕzslav Otruba            Masaryk University, Czechia,2,37,18.50.Vasilios Perdikatsis            Technical University of Crete, Greece,1,57,57.00.Valentin Mihailov            Bulgarian Academy of Sciences, Bulgaria,2,0,-.V Motto Ros            Claude Bernard University Lyon 1, France,2,23,XI.50.Jakub Klus,University of Tennessee at Knoxville, United States            10,184,18.40.Jagdish P Singh,University of Massachusetts Amherst, United States            8,165,20.63.Lev Nagli,University of Florida, United States            14,86,132.86.Valeriy M Nemets,University of Azad Jammu and Kashmir, Pakistan            1,19,19.00.Ulrike Willer            Clausthal University of Technology, Germany,1,185,185.00.Tristan Oliver Nagy            University of Vienna, Austria,2,19,IX.50.Tomáš Kratochvíl            University of Pardubice, Czechia,2,12,6.00.Tobias Reich            Johannes Gutenberg University of Mainz, Germany,1,1,1.00.Timur A Labutin            Lomonosov Moscow State University, Russia,3,139,46.33.Thomas W Schmid            Federal Institute For Materials Research and Testing, Germany,2,29,14.50.Tharwat M El Sherbini            Cairo University, Egypt,1,4,4.00.Teodoro Massimo Miano            University of Bari Aldo Moro, Italy,2,211,105.50.Takunori Taira            Institute for Molecular Science, Japan,1,1,1.00.Tae Hyun Roh            Texas A&M University, United States,1,34,34.00.Sylwia Borowska            Medical University of Białystok, Poland,2,112,56.00.Syahrun Nur Abdulmadjid            Syiah Kuala University, Indonesia,8,78,IX.75.Suresh Kumar Aggarwal            Bhabha Atomic Research Centre, India,1,9,9.00.Sung Mo Nam            Korea Atomic Energy Research Institute, South Korea,1,17,17.00.Suleyman Akman            Istanbul Technical University, Turkey,2,48,24.00.Stewart Sherrit            Jet Propulsion Lab, United States,1,10,10.00.Steve J Hill            University of Plymouth, United Kingdom,2,27,13.50.Stephane Pellerin            Groupe de Recherches sur l'Energétique des Milieux Ionisés, France,4,68,17.00.Stefano Legnaioli            National Research Council, Italy,19,243,65.42.Stefan Karatodorov            Comenius University, Slovakia,2,0,-.Sreedhar Sunku            University of Hyderabad, India,3,12,4.00.Sonja Jovićević            Institute of Physics Belgrade, Serbia,4,66,16.50.Siu-Lung Lui            Tsinghua University, China,2,70,35.00.Simon Carter and An-Min Chen            none,none,9,127,14.XI.Sian Shore and Heikki Juhani Häkkänen            none,none,4,61,15.25.Shuchang Li            Jilin University, China,1,24,24.00.Shivam Gupta            Indian Institute of Technology Roorkee, India,2,4,2.00.Shazia Bashir            Government College University,Pakistan,6,39,VI.50.Sezgin Bakırdere            Yıldız Technical University, Turkey,1,22,22.00.Serpil Kilic            Akdeniz University, Turkey,1,3,3.00.Sergei N Raikov            B.I. Stepanov Institute of Physics, Belarus,1,1,1.00.Seiji Yoshida            Japan Aerospace Exploration Agency, Japan,1,15,15.00.Arijit Sengupta and Satoru Miura            none,none,1,27,27.00.Sara Micheli            Opificio delle Pietre Dure, Italy,1,10,10.00.Samuel Le Berre            Pennsylvania State University, United States,2,36,18.00.Salvador Guirado            University of Malaga, Spain,3,150,50.00.Sachiko Wakabayashi            Japan Aerospace Exploration Agency, Japan,1,10,10.00.Sabrina Loperfido            University of Bari Aldo Moro, Italy,1,40,40.00.S V S Nageswara Rao            University of Hyderabad, India,5,69,13.80.S Abdul Kalam            University of Hyderabad, India,2,61,30.50.Roy A Walters            Ocean Optics (United States), United States,1,129,129.00.Rong-Er Zheng            Ocean University of China, China,5,62,XII.40.Roland Kersting            Ludwig-Maximilians-Universität in Munich, Germany,1,8,8.00.Roberto-Jesús Lasheras            University of Zaragoza, Spain,6,156,26.00.Robert P Lucht            Purdue University System, United States,1,16,16.00.Robert Clough            University of Plymouth, United Kingdom,2,14,7.00.Rinaldi Idroes            Syiah Kuala University, Indonesia,1,5,5.00.Richard G Brereton            University of Bristol, United Kingdom,1,26,26.00.Reto Glaus            Federal Institute For Materials Research and Testing, Germany,3,57,19.00.René Héon            National Research Council Canada, Canada,1,31,31.00.Raymond J Cole            University of British Columbia, Canada,1,1,1.00.Ralf Menzel            University of Potsdam, Germany,1,60,60.00.Rajendhar Junjuri            University of Hyderabad, India,7,31,IV.43.R Hammad Ahmed            Quaid-i-Azam University, Pakistan,5,108,21.60.Qiao Zhang            Beijing University of Chinese Medicine, China,1,16,16.00.Qain-Li Ma            Claude Bernard University Lyon 1, France,1,24,24.00.Ping Meng            Harbin Institute of Technology, China,1,13,13.00.Christopher D Palmer and Phill S Goodall            none,none,8,123,15.38.Philip R Ivancic            Mississippi State University, United States,1,0,-.Petr Knotek            University of Pardubice, Czechia,1,7,7.00.Pengpeng Ma            Northwest Normal University, China,1,4,4.00.Paweł Kościelniak            Jagiellonian University, Poland,2,38,19.00.Pavel A Sdvizhenskii            Prokhorov General Physics Institute, Russia,1,0,-.Paul M Kasili            Oak Ridge National Laboratory, United States,1,2,2.00.Patricia Soupy Dalyander            Water Institute of the Gulf, United States,1,22,22.00.Pascale Dewalle            University of Paris-Saclay, France,1,6,6.00.Panagiotis Siozos            Foundation for Research and Technology Hellas, Greece,4,36,9.00.P Pacheco            University of Atlántico, Colombia,2,5,II.50.Oscar Florencio Gallego            National University of the Northeast, Argentina,1,0,-.Olli Haavisto            Outotec (Finland), Finland,2,15,VII.50.Oliver Lux            German Aerospace Center, Germany,1,12,12.00.Noureddine Melikechi            University of Massachusetts Lowell, United States,4,325,81.25.Noelia Cabaleiro            University of Vigo, Spain,1,2,2.00.Nikolay Kardjilov            Helmholtz-Zentrum Berlin für Materialien und Energie, Germany,2,24,12.00.Nicholas I Boyd            University of Guelph, Canada,1,92,92.00.Nicole Delepine-Gilon            Institute of Analytical Sciences, France,1,12,12.00.Nerea Bordel            University of Oviedo, Spain,3,10,III.33.Michael W Hinds,National University of Central Buenos Aires, Argentina            10,178,17.80.Nasar Ahmed            University of Azad Jammu and Kashmir, Pakistan,4,81,20.25.Nahla A M Hamed            Alexandria University, Egypt,1,2,2.00.Myoung-Kyu Oh            Gwangju Institute of Science and Technology, South Korea,2,32,16.00.Muliadi Ramli            Syiah Kuala University, Indonesia,6,62,X.33.Muhammad Salik            Beijing Jiaotong University, China,8,45,V.63.Muhammad Aslam Baig            Quaid-i-Azam University, Pakistan,1,20,20.00.Moram Sree Satya Bharathi            University of Hyderabad, India,1,2,2.00.Mohammad Javad Torkamany            Iranian National Center for Laser Science and Techology, Iran,2,21,X.50.Mohamed Fikry            Cairo University, Egypt,1,4,4.00.Mohamed A Kasem            Cairo University, Egypt,2,58,29.00.Mirosław Sawczak            Institute of Fluid Flow-Machinery, Poland,2,14,7.00.Mingxing X Jin            Jilin University, China,8,110,13.75.Milivoje Ivković            Institute of Physics Belgrade, Serbia,2,18,9.00.Micheline K Strand            United States Army Research Office, United States,1,0,-.Michaela Remešová            Brno University of Technology, Czechia,1,12,12.00.Michael Oschwald            German Aerospace Center, Germany,1,0,-.Michael Hubeny            Jülich Research Centre, Germany,1,7,7.00.Miaohong He            Guangzhou Institute of Geochemistry, China,1,91,91.00.Melinda Darby Dyar            Mount Holyoke College, United States,1,187,187.00.Meghdad Pirsaheb            Kermanshah University of Medical Sciences, Iran,1,34,34.00.May On Tjia            Bandung Institute of Technology, Indonesia,11,152,13.82.Matthew Weidman            Max Planck Institute of Quantum Optics, Germany,2,19,IX.50.Masaki Ohata            National Institute of Advanced Industrial Science and Technology, Japan,2,13,VI.50.Martin Kyncl            Explosia (Czechia), Czechia,1,34,34.00.Marta Gładysz            Jagiellonian University, Poland,2,38,19.00.Mark C Phillips            University of Arizona, United States,2,28,14.00.Marincan Pardede            Pelita Harapan University, Indonesia,11,92,VIII.36.Maria Margaretha Suliyanti            Indonesian Institute of Sciences, Indonesia,8,79,IX.88.Mari Paz Mateo            University of A Coruña, Spain,3,76,25.33.Marek Sikorski            Adam Mickiewicz University in Poznań, Poland,1,18,18.00.Marco Panesi            University of Illinois Urbana-Champaign, United States,1,2,2.00.Marcela Buchtová            Institute of Animal Physiology and Genetics, Czechia,1,0,-.Manuel García-Heras            Spanish National Research Council, Spain,1,15,15.00.Małgorzata Michalina Brzóska            Medical University of Białystok, Poland,2,112,56.00.Sukesh Roy,Majid Shamsipour            none,1,33,33.00.Magdalena A Iwanicka            Nicolaus Copernicus University, Poland,2,103,51.50.M M Hashemi            Amirkabir University of Technology, Iran,1,2,2.00.Luqman E Oloore            King Fahd University of Petroleum and Minerals, Saudi Arabia,1,45,45.00.Ludger H Wöste            Free University of Berlin, Germany,1,103,103.00.Lucia Daniela Pietanza            National Research Council, Italy,3,51,17.00.Long Ren            North University of China, China,2,11,V.50.Tomitsugu Taguchi,Lilian Cristina Trevizan            none,1,30,30.00.Lian-Bo Guo            Huazhong University of Science and Technology, China,1,15,15.00.Lei Chen            China Academy of Engineering Physics, China,1,0,0.Yoni Groisman,Lawrence Berkeley National Laboratory, United States            2,182,91.00.Laurent P Parès            Research Institute in Astrophysics and Planetology, France,1,309,309.00.Lai-Zhi Sui            Dalian Institute of Chemical Physics, China,2,44,22.00.Shariar Abachi and L Paulard            none,none,1,67,67.00.Kyle C Hartig            University of Florida, United States,2,21,X.50.Kristalia Melessanaki            Foundation for Research and Technology Hellas, Greece,2,263,131.50.Kiran Sankar Maiti            Ludwig-Maximilians-Universität in Munich, Germany,1,0,-.Khoobaram S Choudhari            Manipal Academy of Higher Education, India,1,26,26.00.Kevin Bergler            Iowa State University, United States,1,6,6.00.Ken Marcus            Clemson University, United States,1,14,14.00.Kazuyoshi Kurihara            University of Fukui, Japan,2,19,IX.50.Katsuaki Akaoka            Japan Atomic Energy Agency, Japan,1,16,16.00.Katarzyna Komar            Nicolaus Copernicus University, Poland,1,1,1.00.Karen L Sutton            Procter & Gamble (United Kingdom), United Kingdom,2,46,23.00.Kadhim Abdulwahid Aadim            University of Baghdad, Iraq,2,0,-.Juri Agresti            National Research Council, Italy,8,86,X.75.Jun-Jie Yan            Xi'an Jiaotong University, China,3,60,20.00.Jun Duan            Huazhong University of Science and Technology, China,1,15,15.00.Julia Waack            Robert Gordon University, United Kingdom,2,14,7.00.Juan D Rosales            Complutense University of Madrid, Spain,1,79,79.00.Jovan Ciganovic            University of Belgrade, Serbia,5,32,VI.40.Joseph A Miragliotta            Johns Hopkins University Applied Physics Laboratory, United States,1,8,8.00.José Miguel Vadillo            University of Malaga, Spain,3,218,72.67.José Carlos Diaz Rosado            University of Paris-Sud, France,1,5,5.00.Jorge Pisonero            University of Oviedo, Spain,5,28,V.60.Jordi Vives I Batlle            Belgian Nuclear Research Centre, Belgium,1,4,4.00.Jon Scaffidi            University of Pittsburgh, United States,2,233,116.50.John Lavery and Abdul Jabbar            none,none,2,1,0.50.John A Maxwell and Edwin Alexander Yates,none,none,1,92,92.00.Johan Vellekoop            KU Leuven, Belgium,1,4,4.00.Joachim Koch            ETH Zurich, Switzerland,3,18,6.00.Jin-Ping Zhang            Hebei University, China,1,0,0.Aleš Hrdlička,Jilin University, China            9,115,XII.78.Jiasheng Wang            Beijing Jiaotong University, China,2,6,3.00.Jiajia Hou            Shanxi University, China,2,15,VII.50.Jeremie Lasue            Research Institute in Astrophysics and Planetology, France,3,502,167.33.Jelena J Mutić            University of Belgrade, Serbia,1,10,10.00.Jean-Paul Mosnier            Dublin City University, Ireland,2,35,17.50.Jean Denis Parisse            École de l'air, France,1,0,-.Jason Loiseau            Royal Military College of Canada, Canada,1,1,1.00.Jana Kolar            Consortium of the Trieste Science and Technology Research Area, Italy,1,22,22.00.James H Burton            University of Wisconsin–Madison, United States,1,45,45.00.Jakub Vrábel            Brno University of Technology, Czechia,4,56,14.00.Jack Zhou            University of Connecticut, United States,1,29,29.00.J Bengoechea            Universidad Publica De Navarra, Spain,2,208,104.00.IV.50            Hyungrok Do,Seoul National University, South Korea,2,47.Ismail Akdeniz            Bozok University, Turkey,1,22,22.00.Isabelle Monnet            Hôpital Intercommunal de Créteil, France,1,0,0.Nasrullah Idris,Institute of Structure of Matter, Italy            9,298,33.11.Igor V Cravetchi            University of Alberta, Canada,2,48,24.00.T Linsmeyer,Idaho National Laboratory,United States,1,18,18.00.Chukwujindu Maxwell Azubuike Iwegbue            Delta State University, Nigeria,4,60,15.00.Christopher D Palmer            Wadsworth Center, United States,8,160,20.00.Christoph Haisch            Technical University of Munich, Germany,6,286,47.67.Chongming Wang            Coventry University, United Kingdom,1,1,1.00.Chi Zhang            Johns Hopkins University, United States,1,13,13.00.Chen Deying            Shandong University, China,1,0,-.Changho Seo            Pohang University of Science and Technology, South Korea,1,5,5.00.Hyo Hyun Cho            Changwon National University, South Korea,1,12,12.00.Hubert Du"
dataset = dataset.replace("            ", ",").replace(", ", ",").replace(",-.",",0.").replace(",-,", ",0,")
matches = re.findall(entry_stop, dataset)

for match in matches:
    index = dataset.find(match) + 1
    entry_str = dataset[0: index]
    dataset = dataset[index+1:]
    if entry_str.count(",") != 5:
        print("INVALID ENTRY")
        print(entry_str)
    #parse_entry(entry_str)

