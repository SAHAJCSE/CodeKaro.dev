# OpenJDK 17 JDK base image with Ubuntu Jammy
FROM eclipse-temurin:17-jdk-jammy

# Install Python 3 (stdlib only - no pip dependencies required)
RUN apt-get update && \
    apt-get install -y --no-install-recommends python3 && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Create a non-root user for secure code execution
RUN useradd -m -u 1000 runneruser

# Copy common Java judge harness and precompile it
COPY common/Judge.java /app/common/Judge.java
RUN javac -J-XX:TieredStopAtLevel=1 -J-Xmx128m /app/common/Judge.java


# Copy problem test suites and ensure ONLY Test.java files are retained
# Solutions and statements are stripped; reference/ is excluded via .dockerignore
COPY problems/ /app/problems/
RUN find /app/problems -type f ! -name "Test.java" -delete

# Copy runner backend code
COPY runner/ /app/runner/

# Grant appropriate permissions
RUN chown -R runneruser:runneruser /app

# Switch to non-root user
USER runneruser

ENV PORT=8000 \
    PYTHONUNBUFFERED=1

EXPOSE 8000

CMD ["python3", "runner/server.py"]
