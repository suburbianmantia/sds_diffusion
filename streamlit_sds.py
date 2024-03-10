import streamlit as st
st.title("SDS Clinical and SDS Biopsy for sarcoidosis diagnosis")
st.markdown("Here is a free implementation of the SDS score for sarcoidosis diagnosis")
st.subheader("Lung")
high_pro_lung = st.radio("Following features are present (select one if present): ",
                         ["None","CXR: bilateral hilar adenopathy",
                          "Chest CT: perilymphatic nodules",
                          "Chest CT: symmetrical hilar/mediastinal adenopathy",
                          "PET/Gallium-67: mediastinal/hilar enhancement"])
least_pro_lung = st.radio("Following features are present (select one if present): ",
                         ["None","CXR: diffuse infiltrates",
                          "CXR: upper lobe fibrosis",
                          "BAL: lymphocytic alveolitis",
                          "BAL: elevated CD4/CD8 ratio",
                         "PET/Gallium-67: diffuse parenchymal lung enhancement",
                         "TBNA: lymphoid aggregates/giant cells"])

if high_pro_lung in  ["CXR: bilateral hilar adenopathy",
                          "Chest CT: perilymphatic nodules",
                          "Chest CT: symmetrical hilar/mediastinal adenopathy",
                          "PET/Gallium-67: mediastinal/hilar enhancement"]:
    pro_lung = 3
elif least_pro_lung in ["CXR: diffuse infiltrates",
                          "CXR: upper lobe fibrosis",
                          "BAL: lymphocytic alveolitis",
                          "BAL: elevated CD4/CD8 ratio",
                         "PET/Gallium-67: diffuse parenchymal lung enhancement",
                         "TBNA: lymphoid aggregates/giant cells"] and high_pro_lung not in ["CXR: bilateral hilar adenopathy",
                          "Chest CT: perilymphatic nodules",
                          "Chest CT: symmetrical hilar/mediastinal adenopathy",
                          "PET/Gallium-67: mediastinal/hilar enhancement"] :
    pro_lung = 2
else: 
    pro_lung = 0

lung_granu = st.radio("Granuloma is present on lung biopsy",["No","Yes"])

if lung_granu == 'Yes':
    pro_lung_granu = 5
elif lung_granu == 'No':
    pro_lung_granu = 0
    
st.subheader("Neurologic")
high_pro_neuro = st.radio("Following features are present (select one if present): ",
                         ["None","Clinical syndrome consistent with granulomatous inflammation of the meninges, \n brain, ventricular (CSF) system, cranial nerves, pituitary gland, spinal cord, \ncerebral vasculature or nerve roots \nAND \nAn abnormal MRI characteristic of neurosarcoidosis, defined as exhibiting abnormal\nenhancement following the administration of gadolinium or a cerebrospinal fluid \nexam demonstrating inflammation"])
least_pro_neuro = st.radio("Following features are present (select one if present): ",
                         ["None","Isolated facial palsy, negative MRI ",
                          "Clinical syndrome consistent with granulomatous inflammation of the meninges, \nbrain, ventricular (CSF) system, cranial nerves, pituitary gland, spinal cord, \ncerebral vasculature, nerve roots but without characteristic MRI or CSF findings "])

if high_pro_neuro in  ["Clinical syndrome consistent with granulomatous inflammation of the meninges, \nbrain, ventricular (CSF) system, cranial nerves, pituitary gland, spinal cord, \ncerebral vasculature or nerve roots \nAND \nAn abnormal MRI characteristic of neurosarcoidosis, defined as exhibiting abnormal\nenhancement following the administration of gadolinium or a cerebrospinal fluid \nexam demonstrating inflammation"]:
    pro_neuro = 3
elif least_pro_neuro in ["Isolated facial palsy, negative MRI ",
                          "Clinical syndrome consistent with granulomatous inflammation of the meninges, \nbrain, ventricular (CSF) system, cranial nerves, pituitary gland, spinal cord, \ncerebral vasculature, nerve roots but without characteristic MRI or CSF findings "] :
    pro_neuro = 2
else: 
    pro_neuro = 0

neuro_granu = st.radio("Granuloma is present on neuro biopsy",["No","Yes"])

if neuro_granu == 'Yes':
    pro_neuro_granu = 5
elif neuro_granu == 'No':
    pro_neuro_granu = 0

st.subheader("Non thoracic lymph nodes")

least_pro_lymph = st.radio("Following features are present (select one if present): ",
                         ["None","Multiple enlarged palpable cervical or epitrochlear lymph nodes without B symptoms",
                          "Enlarged lymph nodes identified by imaging in at least 2 peripheral or visceral lymph \nnode stations without B symptoms "])

if least_pro_lymph in ["Multiple enlarged palpable cervical or epitrochlear lymph nodes without B symptoms",
                          "Enlarged lymph nodes identified by imaging in at least 2 peripheral or visceral lymph \nnode stations without B symptoms "] :
    pro_lymph = 2
else: 
    pro_lymph = 0

lymph_granu = st.radio("Granuloma is present on lymph node biopsy",["No","Yes"])

if lymph_granu == 'Yes':
    pro_lymph_granu = 5
elif lymph_granu == 'No':
    pro_lymph_granu = 0


st.subheader("Kidney")

least_pro_kidney = st.radio("Following features are present (select one if present): ",
                         ["None","Treatment-responsive renal failure with no other risk factors.",
                          "Treatment-responsive renal failure in patient with diabetes and/or hypertension."])

if least_pro_kidney in ["Treatment-responsive renal failure with no other risk factors.",
                          "Treatment-responsive renal failure in patient with diabetes and/or hypertension."] :
    pro_kidney = 2
else: 
    pro_kidney = 0

kidney_granu = st.radio("Granuloma is present on kidney biopsy",["No","Yes"])

if kidney_granu == 'Yes':
    pro_kidney_granu = 5
elif kidney_granu == 'No':
    pro_kidney_granu = 0

st.subheader("Cardiac")


least_pro_heart = st.radio("Following features are present (select one if present): ",
                         ["None","Treatment responsive CM or AVNB",
                          "Reduced LVEF in the absence of other clinical risk factors",
                         "Spontaneous or inducible sustained VT with no other risk factor",
                         "Mobitz type II or 3rd degree heart block ",
                         "Patchy uptake on dedicated cardiac PET ",
                         "Delayed enhancement on CMR ",
                         "Positive gallium uptake",
                         "Defect on perfusion scintigraphy or SPECT scan",
                         "T2 prolongation on CMR"])

if least_pro_heart in ["Treatment responsive CM or AVNB",
                          "Reduced LVEF in the absence of other clinical risk factors",
                         "Spontaneous or inducible sustained VT with no other risk factor",
                         "Mobitz type II or 3rd degree heart block ",
                         "Patchy uptake on dedicated cardiac PET ",
                         "Delayed enhancement on CMR ",
                         "Positive gallium uptake",
                         "Defect on perfusion scintigraphy or SPECT scan",
                         "T2 prolongation on CMR"] :
    pro_heart = 2
else: 
    pro_heart = 0

heart_granu = st.radio("Granuloma is present on cardiac biopsy",["No","Yes"])

if heart_granu == 'Yes':
    pro_heart_granu = 5
elif heart_granu == 'No':
    pro_heart_granu = 0

st.subheader("Skin")
high_pro_skin = st.radio("Following features are present (select one if present): ",
                         ["None","Lupus pernio"])
least_pro_skin = st.radio("Following features are present (select one if present): ",
                         ["None","Subcutaneous nodules or plaques Inflammatory papules within a scar or tattoo",
                          "Violaceous or erythematous annular lesions",
                         "Violaceous or erythematous macular, papular lesions around the eyes, nose, or mouth"])

if high_pro_skin in  ["Lupus pernio"]:
    pro_skin = 3
elif least_pro_skin in ["Subcutaneous nodules or plaques Inflammatory papules within a scar or tattoo",
                          "Violaceous or erythematous annular lesions",
                         "Violaceous or erythematous macular, papular lesions around the eyes, nose, or mouth"] :
    pro_skin = 2
else: 
    pro_skin = 0

skin_granu = st.radio("Granuloma is present on skin biopsy",["No","Yes"])

if skin_granu == 'Yes':
    pro_skin_granu = 5
elif skin_granu == 'No':
    pro_skin_granu = 0


st.subheader("Eyes")
high_pro_eye = st.radio("Following features are present (select one if present): ",
                         ["None","Uveitis",
                         "Optic neuritis",
                         "Mutton fat keratic precipitates ",
                          "Iris nodules",
                         "Snowball/string of pearls (pars planitis)"])
least_pro_eye = st.radio("Following features are present (select one if present): ",
                         ["None","Lacrimal gland swelling ",
                          "Trabecular meshwork nodules",
                         "Retinitis",
                         "Scleritis",
                         "Multiple chorioretinal peripheral lesions",
                         "Adnexal nodularity",
                         "Candle wax drippings", "None"])

if high_pro_eye in  ["Uveitis",
                         "Optic neuritis",
                         "Mutton fat keratic precipitates ",
                          "Iris nodules",
                         "Snowball/string of pearls (pars planitis)"]:
    pro_eye = 3
elif least_pro_eye in ["Lacrimal gland swelling ",
                          "Trabecular meshwork nodules",
                         "Retinitis",
                         "Scleritis",
                         "Multiple chorioretinal peripheral lesions",
                         "Adnexal nodularity",
                         "Candle wax drippings"] :
    pro_eye = 2
else: 
    pro_eye = 0

eye_granu = st.radio("Granuloma is present on eye biopsy",["No","Yes"])

if eye_granu == 'Yes':
    pro_eye_granu = 5
elif eye_granu == 'No':
    pro_eye_granu = 0
    

st.subheader("Liver")

least_pro_liver = st.radio("Following features are present (select one if present): ",
                         ["None","Abdominal imaging demonstrating hepatomegaly",
                          "Abdominal imaging demonstrating hepatic nodules",
                         "Alkaline phosphatase >3 times ULN"])

if least_pro_liver in ["Abdominal imaging demonstrating hepatomegaly",
                          "Abdominal imaging demonstrating hepatic nodules",
                         "Alkaline phosphatase >3 times ULN"] :
    pro_liver = 2
else: 
    pro_liver = 0

liver_granu = st.radio("Granuloma is present on liver biopsy",["No","Yes"])

if liver_granu == 'Yes':
    pro_liver_granu = 5
elif liver_granu == 'No':
    pro_liver_granu = 0

st.subheader("Bone marrow")

least_pro_bone = st.radio("Following features are present (select one if present): ",
                         ["None","Diffuse PET uptake"])

if least_pro_bone in ["Diffuse PET uptake"] :
    pro_bone = 2
else: 
    pro_bone = 0

bone_granu = st.radio("Granuloma is present on bone marrow biopsy",["No","Yes"])

if bone_granu == 'Yes':
    pro_bone_granu = 5
elif bone_granu == 'No':
    pro_bone_granu = 0

st.subheader("Spleen")

least_pro_spleen = st.radio("Following features are present (select one if present): ",
                         ["None","Low attenuation nodules on CT",
                          "PET/gallium-67 uptake in splenic nodules ",
                         "Splenomegaly on imaging or physical examination"])

if least_pro_spleen in ["Low attenuation nodules on CT",
                          "PET/gallium-67 uptake in splenic nodules ",
                         "Splenomegaly on imaging or physical examination"] :
    pro_spleen = 2
else: 
    pro_spleen = 0

spleen_granu = st.radio("Granuloma is present on spleen biopsy",["No","Yes"])

if spleen_granu == 'Yes':
    pro_spleen_granu = 5
elif spleen_granu == 'No':
    pro_spleen_granu = 0

st.subheader("Joints")
high_pro_joint = st.radio("Following features are present (select one if present): ",
                         ["None","Typical radiographic features (trabecular pattern, osteolysis, cysts/punched out lesions)"])
least_pro_joint = st.radio("Following features are present (select one if present): ",
                         ["None","Dactylitis ",
                          "Nodular tenosynovitis ",
                         "Positive PET, MRI, or gallium-67 bone imaging "
                         ])

if high_pro_joint in  ["Typical radiographic features (trabecular pattern, osteolysis, cysts/punched out lesions)"]:
    pro_joint = 3
elif least_pro_joint in ["Dactylitis ",
                          "Nodular tenosynovitis ",
                         "Positive PET, MRI, or gallium-67 bone imaging "
                         ] :
    pro_joint = 2
else: 
    pro_joint = 0

joint_granu = st.radio("Granuloma is present on joint biopsy",["No","Yes"])

if joint_granu == 'Yes':
    pro_joint_granu = 5
elif joint_granu == 'No':
    pro_joint_granu = 0

st.subheader("ENT")

least_pro_ENT = st.radio("Following features are present (select one if present): ",
                         ["None","Granulomatous changes on direct laryngoscopy  ",
                          "Consistent imaging studies (e.g. sinonasal erosion, mucoperiosteal thickening, positive PET scan) "])

if least_pro_ENT in ["Granulomatous changes on direct laryngoscopy  ",
                          "Consistent imaging studies (e.g. sinonasal erosion, mucoperiosteal thickening, positive PET scan) "] :
    pro_ENT = 2
else: 
    pro_ENT = 0

ENT_granu = st.radio("Granuloma is present on ENT biopsy",["No","Yes"])

if ENT_granu == 'Yes':
    pro_ENT_granu = 5
elif ENT_granu == 'No':
    pro_ENT_granu = 0


st.subheader("Salivary glands")
high_pro_salivary = st.radio("Following features are present (select one if present): ",
                         ["None","Positive gallium-67 scan (“Panda sign”) ",
                         "Positive PET scan of the parotid glands "])
least_pro_salivary = st.radio("Following features are present (select one if present): ",
                         ["None","Symmetrical parotitis with syndrome of mumps",
                          "Enlarged salivary glands"])

if high_pro_salivary in  ["Positive gallium-67 scan (“Panda sign”) ",
                         "Positive PET scan of the parotid glands "]:
    pro_salivary = 3
elif least_pro_salivary in ["Symmetrical parotitis with syndrome of mumps",
                          "Enlarged salivary glands" ] :
    pro_salivary = 2
else: 
    pro_salivary = 0

salivary_granu = st.radio("Granuloma is present on salivary gland biopsy",["No","Yes"])

if salivary_granu == 'Yes':
    pro_salivary_granu = 5
elif salivary_granu == 'No':
    pro_salivary_granu = 0

st.subheader("Muscles")
least_pro_muscle = st.radio("Following features are present (select one if present): ",
                         ["None","Positive imaging (MRI, Gallium-67) ",
                          "Palpable muscle masses"])

if least_pro_muscle in ["Positive imaging (MRI, Gallium-67) ",
                          "Palpable muscle masses"] :
    pro_muscle = 2
else: 
    pro_muscle = 0

muscle_granu = st.radio("Granuloma is present on muscle biopsy",["No","Yes"])

if muscle_granu == 'Yes':
    pro_muscle_granu = 5
elif muscle_granu == 'No':
    pro_muscle_granu = 0

st.subheader("Calcium")
high_pro_calcium = st.radio("Following features are present (select one if present): ",
                         ["None","Hypercalcemia plus all of the following: \na) a normal serum PTH level; \nb) a normal or increased 1,25-OH dihydroxy vitamin D level; \nc) a low 25-OH vitamin D level",
                         "Hypercalciuria plus all of the following: \na) a normal serum PTH level; \nb) a normal or increased 1,25-OH dihydroxy vitamin D level; \nc) a low 25-OH vitamin D level"])
least_pro_calcium = st.radio("Following features are present (select one if present): ",
                         ["None","Nephrolithiasis plus all of the following: \n a) a normal serum PTH level; \nb) a normal or increased 1,25-OH dihydroxy vitamin D level; \nc) a low 25-OH vitamin D level",
                          "Hypercalciuria without serum PTH and 25 and 1,25 vitamin D levels",
                         "Nephrolithiasis with calcium stones, without serum PTH and 25 and 1,25 vitamin D levels"])

if high_pro_calcium in  ["Hypercalcemia plus all of the following: \na) a normal serum PTH level; \nb) a normal or increased 1,25-OH dihydroxy vitamin D level; \nc) a low 25-OH vitamin D level",
                         "Hypercalciuria plus all of the following: \na) a normal serum PTH level; \nb) a normal or increased 1,25-OH dihydroxy vitamin D level; \nc) a low 25-OH vitamin D level"]:
    pro_calcium = 3
elif least_pro_calcium in ["Nephrolithiasis plus all of the following: \n a) a normal serum PTH level; \nb) a normal or increased 1,25-OH dihydroxy vitamin D level; \nc) a low 25-OH vitamin D level",
                          "Hypercalciuria without serum PTH and 25 and 1,25 vitamin D levels",
                         "Nephrolithiasis with calcium stones, without serum PTH and 25 and 1,25 vitamin D levels"] :
    pro_calcium = 2
else: 
    pro_calcium = 0

st.subheader("Lofgren")
lofgren = st.radio("Lofgren is present", ["No","Yes"])
if lofgren == "Yes":
    pro_lofgren = 5
else: 
    pro_lofgren = 0
    
SDS_biopsy = pro_lung+pro_lung_granu+pro_neuro+pro_neuro_granu+pro_lymph+pro_lymph_granu+pro_kidney+pro_kidney_granu+pro_heart+pro_heart_granu+pro_skin+pro_skin_granu+pro_eye+pro_eye_granu+pro_liver+pro_liver_granu+pro_bone+pro_bone_granu+pro_spleen+pro_spleen_granu+pro_joint+pro_joint_granu+pro_ENT+pro_ENT_granu+pro_salivary+pro_salivary_granu+pro_muscle+pro_muscle_granu+pro_calcium+pro_lofgren
SDS_clinical = pro_lung+pro_neuro+pro_lymph+pro_kidney+pro_heart+pro_skin+pro_eye+pro_liver+pro_bone+pro_spleen+pro_joint+pro_ENT+pro_salivary+pro_muscle+pro_calcium

st.write("SDS clinical is: ", SDS_clinical)

st.write("SDS biopsy is: ", SDS_biopsy)

st.subheader("Clinical diagnosis")
if SDS_clinical > 9: 
    st.write("Sarcoidosis")
elif SDS_clinical <3:
    st.write("Sarcoidosis less likely")
else:
    biopsy_decision = st.radio("Was biopsy performed?",["Yes, consistent with sarcoidosis","No", "Yes and negative"])
    if biopsy_decision == "No" or biopsy_decision == "Yes and negative":
        if SDS_clinical>4:
            st.write('Sarcoidosis is probable')
        else: 
            st.write('Observe')      
    else:
        st.write('Sarcoidosis likely')

st.subheader("Biopsy diagnosis")
if SDS_biopsy > 11: 
    st.write("Sarcoidosis")
elif SDS_clinical <=5:
    st.write("Sarcoidosis less likely")
else:
    infection_decision = st.radio("Tuberculosis, fungal infection and malignancy ruled out?",["Yes","No"])
    if infection_decision == "No":
        st.write('Sarcoidosis is not probable')
    else: 
        st.write('Sarcoidosis')

    




