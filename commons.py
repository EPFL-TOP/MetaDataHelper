data_dirs=["analysis_files", "configuration_files", "raw_files"]

data_types={"microscopy":["in_vivo","in_vitro"], "sequencing":["CUTandTAG","scRNA-seq","scMultiome-seq"]}


metadata_common = {
    "authors":[],
    "laboratory_contributors":[],
    "external_contributors":[],
    "experiment_name":"",
    "starting_date":{
        "year":"",
        "month":"",
        "day":""},
    "status":[],
    "experimental_tags":[],
    "fish_lines":[],
    "mutations":[],
    "phenotypes":[],
    "slim_ids":[],
    "pyrat_ids":[],
    "bioarxiv_tags":[],
    "journal_tags":[],
    "zenodo_tags":[]
}

metadata_invitro = {
    "coating":[],
    "treatment":[],
    "npositions":""
}

metadata_invivo = {
    "coating":[],
    "treatment":[],
    "npositions":""
}

metadata_scrna = {
}

metadata_scmultiome = {

}

metadata_cutandtag = {

}