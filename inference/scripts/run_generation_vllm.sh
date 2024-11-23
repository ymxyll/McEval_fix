
COMPLETE_DATA_PATH='../../python_eval_data/generate'

MODEL_DIR='<model_dir>'

OUT_DIR='../../out/wait_to_split'

python ../inference_vllm.py \
    --data_path $COMPLETE_DATA_PATH \
    --base_model $MODEL_DIR \
    --task 'generation' \
    --outdir $OUT_DIR