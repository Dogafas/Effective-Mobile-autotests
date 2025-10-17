#!/bin/bash

echo "Building and running tests..."
docker-compose build tests
docker-compose run --rm tests

echo ""
echo "Starting Allure report service..."
docker-compose up -d allure

echo ""
echo "Waiting for Allure service to start..."
sleep 5

echo ""
echo "Report available at: http://localhost:4040/allure-docker-service/projects/default/reports/latest/index.html"
echo "To stop Allure service: docker-compose down"