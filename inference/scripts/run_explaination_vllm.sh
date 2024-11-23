
MODEL_DIR='<model_dir>'

COMPLETE_DATA_PATH='../../python_eval_data/explanation'

OUT_DIR1='../../out/wait_to_split/stage1'


python ../inference_vllm.py \
    --data_path $COMPLETE_DATA_PATH \
    --base_model $MODEL_DIR \
    --task 'explain' \
    --outdir $OUT_DIR1

OUT_DIR2='../../out/wait_to_split/stage2'

python ../gen_stage2_instruction.py \
    --data_path $OUT_DIR1 \
    --outdir $OUT_DIR2


OUT_DIR3='../../out/wait_to_split'

python ../inference_vllm.py \
    --data_path $OUT_DIR2 \
    --base_model $MODEL_DIR \
    --task 'explain' \
    --outdir $OUT_DIR3