from fastapi import APIRouter, status

from apps.app.models import *


router = APIRouter()


@router.post("/job/create/", status_code=status.HTTP_201_CREATED)
async def create_job(job: job_pydantic):
    job = await Job.create(**job.dict())
    return job


@router.get("/jobs/", status_code=status.HTTP_200_OK)
async def get_jobs():
    return await job_pydanticOut.from_queryset(Job.all())


@router.get("/job/{job_id}")
async def get_job(job_id: int):
    return await job_pydanticOut.from_queryset_single(Job.get(id=job_id))


@router.put("/job/{job_id}")
async def update_job(job_id: int, job: job_pydanticUp):
    await Job.filter(id=job_id).update(**job.dict())
    return await job_pydanticOut.from_queryset_single(Job.get(id=job_id))
