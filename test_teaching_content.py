#!/usr/bin/env python3
"""
Test script to explore teaching content endpoints in WebUntis API.
"""

import asyncio
import json
from datetime import datetime, timedelta
from custom_components.webuntis.utils.web_untis_extended import ExtendedSession

async def test_teaching_content():
    """Test teaching content endpoints."""
    
    # You'll need to provide your WebUntis credentials
    server = "your_server"  # e.g., "webuntis.com" 
    school = "your_school"  # Your school name
    username = "your_username"
    password = "your_password"
    
    print("Testing WebUntis Teaching Content Endpoints")
    print("=" * 50)
    
    try:
        # Create session
        session = ExtendedSession(
            server=server,
            username=username,  
            password=password,
            school=school,
            useragent="HomeAssistant-WebUntis"
        )
        
        # Login
        print("Logging in...")
        session.login()
        print("✓ Login successful")
        
        # Set date range (last week)
        end_date = datetime.now()
        start_date = end_date - timedelta(days=7)
        
        print(f"Date range: {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}")
        print()
        
        # 1. Test existing lesson content fields
        print("1. Testing existing lesson content fields...")
        print("-" * 40)
        
        lesson_details = session.get_lesson_content_details(start_date, end_date)
        
        if isinstance(lesson_details, dict) and "error" in lesson_details:
            print(f"Error getting lesson details: {lesson_details['error']}")
        else:
            print(f"Found {len(lesson_details)} lessons")
            
            # Show lessons with content
            lessons_with_content = []
            for lesson in lesson_details:
                has_content = any([
                    lesson.get("lstext"),
                    lesson.get("substText"), 
                    lesson.get("lsnumber"),
                    lesson.get("text"),
                    lesson.get("info"),
                    lesson.get("content"),
                    lesson.get("topic"),
                    lesson.get("teachingContent"),
                    lesson.get("lessonContent")
                ])
                
                if has_content:
                    lessons_with_content.append(lesson)
            
            print(f"Lessons with content: {len(lessons_with_content)}")
            
            # Show sample content
            if lessons_with_content:
                print("\nSample lesson with content:")
                sample = lessons_with_content[0]
                for key, value in sample.items():
                    if value is not None and value != []:
                        print(f"  {key}: {value}")
            else:
                print("No lessons found with content fields")
        
        print("\n" + "=" * 50)
        
        # 2. Test potential teaching content endpoints
        print("2. Testing potential teaching content endpoints...")
        print("-" * 50)
        
        endpoint_results = session.explore_teaching_content_endpoints(start_date, end_date)
        
        for endpoint, result in endpoint_results.items():
            print(f"\nEndpoint: {endpoint}")
            if result["success"]:
                print(f"  ✓ Success - Type: {result['type']}, Length: {result['length']}")
                if "keys" in result:
                    print(f"  Keys: {result['keys']}")
                elif "sample_keys" in result:
                    print(f"  Sample keys: {result['sample_keys']}")
                
                # Show sample data for successful endpoints
                if result["length"] != "N/A" and result["length"] > 0:
                    data = result["data"]
                    if isinstance(data, list) and len(data) > 0:
                        print(f"  Sample data: {json.dumps(data[0], indent=2)[:200]}...")
                    elif isinstance(data, dict):
                        print(f"  Data: {json.dumps(data, indent=2)[:200]}...")
            else:
                print(f"  ✗ Failed - Error: {result['error']}")
        
        # 3. Test standard homework/exam endpoints for comparison
        print("\n" + "=" * 50)
        print("3. Testing known working endpoints (homework/exams)...")
        print("-" * 50)
        
        # Test homework endpoint
        try:
            homeworks = session.get_homeworks(start_date, end_date)
            print(f"Homeworks endpoint: ✓ Success - {len(homeworks) if isinstance(homeworks, list) else 'N/A'} items")
            if isinstance(homeworks, list) and len(homeworks) > 0:
                print(f"  Sample homework keys: {list(homeworks[0].keys()) if isinstance(homeworks[0], dict) else 'not_dict'}")
        except Exception as e:
            print(f"Homeworks endpoint: ✗ Failed - {str(e)}")
        
        # Test exams endpoint
        try:
            exams = session.get_exams(start_date, end_date)
            print(f"Exams endpoint: ✓ Success - {len(exams) if isinstance(exams, list) else 'N/A'} items")
            if isinstance(exams, list) and len(exams) > 0:
                print(f"  Sample exam keys: {list(exams[0].keys()) if isinstance(exams[0], dict) else 'not_dict'}")
        except Exception as e:
            print(f"Exams endpoint: ✗ Failed - {str(e)}")
        
        # Logout
        session.logout()
        print("\n✓ Logged out")
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    print("WebUntis Teaching Content Explorer")
    print("=" * 50)
    print()
    print("Before running this script, you need to:")
    print("1. Install webuntis library: pip install webuntis")
    print("2. Update the credentials in the script")
    print("3. Make sure your WebUntis instance is accessible")
    print()
    
    # Uncomment the line below and update credentials to run
    # asyncio.run(test_teaching_content())
    print("Please update credentials and uncomment the last line to run the test.")
