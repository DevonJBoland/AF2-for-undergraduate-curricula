python3 alphafold.py \
 --data_dir=$DOWNLOAD_DIR  --use_gpu_relax=False \
 --uniref90_database_path=$DOWNLOAD_DIR/uniref90/uniref90.fasta \
 --uniclust30_database_path=$DOWNLOAD_DIR/uniclust30/uniclust30_2021_03/UniRef30_2021_03 \
 --mgnify_database_path=$DOWNLOAD_DIR/mgnify/mgy_clusters_2018_12.fa \
 --bfd_database_path=$DOWNLOAD_DIR/bfd/bfd_metaclust_clu_complete_id30_c90_final_seq.sorted_opt \
 --pdb70_database_path=$DOWNLOAD_DIR/pdb70/pdb70 \
 --template_mmcif_dir=$DOWNLOAD_DIR/pdb_mmcif/mmcif_files \
 --obsolete_pdbs_path=$DOWNLOAD_DIR/pdb_mmcif/obsolete.dat \
 --model_preset=monomer_ptm \
 --max_template_date=$max_template_date \
 --db_preset=full_db \
 --output_dir=$output_dir \
 --fasta_paths=$protein_fasta

# This line command will run a python script to plot our pLDDT and pAE plots
run_AlphaPickle.py -od $output_dir/$pickle_out_dir
