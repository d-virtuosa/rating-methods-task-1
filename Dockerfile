FROM python:3.11-slim
RUN pip install Flask
WORKDIR /work
COPY api_calc.py .
EXPOSE 5000
CMD ["python", "api_calc.py"]
