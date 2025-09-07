#!/usr/bin/env python3
"""
Script to explore WebUntis API endpoints and discover what's available
"""

def explore_webuntis_api():
    """
    Explore various WebUntis API endpoints to find what's available
    """
    
    # Common WebUntis API endpoints to test
    potential_endpoints = [
        # Standard JSON-RPC endpoints
        "/WebUntis/jsonrpc.do",
        
        # REST API endpoints (discovered patterns)
        "/WebUntis/api/homeworks/lessons",
        "/WebUntis/api/exams", 
        "/WebUntis/api/lessons",
        "/WebUntis/api/timetable",
        "/WebUntis/api/subjects",
        "/WebUntis/api/teachers",
        "/WebUntis/api/classes",
        "/WebUntis/api/rooms",
        "/WebUntis/api/students",
        "/WebUntis/api/periods",
        "/WebUntis/api/schoolyears",
        "/WebUntis/api/holidays",
        "/WebUntis/api/timegrid",
        "/WebUntis/api/absences",
        "/WebUntis/api/substitutions",
        "/WebUntis/api/events",
        "/WebUntis/api/curriculum",
        "/WebUntis/api/lessoninfo",
        "/WebUntis/api/lessontopic",
        "/WebUntis/api/lessontext",
        "/WebUntis/api/classbookentries",
        "/WebUntis/api/classbook",
        "/WebUntis/api/content",
        "/WebUntis/api/materials",
        "/WebUntis/api/resources",
        "/WebUntis/api/news",
        "/WebUntis/api/messages",
        "/WebUntis/api/announcements"
    ]
    
    print("=== Potential WebUntis API Endpoints ===")
    print("These are common endpoints that might exist in WebUntis:")
    
    for endpoint in potential_endpoints:
        print(f"  {endpoint}")
    
    print("\n=== How to Test These Endpoints ===")
    print("1. Use browser developer tools:")
    print("   - Log into WebUntis web interface")
    print("   - Open Developer Tools (F12) -> Network tab")
    print("   - Navigate around the interface")
    print("   - Look for API calls in the Network tab")
    
    print("\n2. Test with authenticated session:")
    print("   - Copy the JSESSIONID from browser cookies")
    print("   - Use requests.get() with the session cookie")
    
    print("\n3. Look for lesson topics/content endpoints:")
    print("   - /WebUntis/api/lessontopic")
    print("   - /WebUntis/api/lessontext") 
    print("   - /WebUntis/api/classbookentries")
    print("   - /WebUntis/api/classbook")
    print("   - /WebUntis/api/content")
    
    return potential_endpoints

def create_test_function():
    """
    Create a test function to add to ExtendedSession
    """
    
    test_code = '''
    def explore_endpoints(self, start, end):
        """
        Test various endpoints to see what's available
        
        :param start: Start date
        :param end: End date  
        :return: Dictionary of endpoint responses
        """
        
        endpoints_to_test = [
            "/WebUntis/api/lessontopic",
            "/WebUntis/api/lessontext", 
            "/WebUntis/api/classbookentries",
            "/WebUntis/api/classbook",
            "/WebUntis/api/content",
            "/WebUntis/api/materials",
            "/WebUntis/api/lessons",
            "/WebUntis/api/subjects",
            "/WebUntis/api/curriculum"
        ]
        
        params = {
            "startDate": start.strftime("%Y%m%d"),
            "endDate": end.strftime("%Y%m%d"),
        }
        
        results = {}
        
        for endpoint in endpoints_to_test:
            try:
                response = self._send_custom_request(endpoint, params)
                results[endpoint] = {
                    "success": True,
                    "data": response,
                    "keys": list(response.keys()) if isinstance(response, dict) else "not_dict"
                }
                print(f"✅ {endpoint}: Success")
                if isinstance(response, dict):
                    print(f"   Keys: {list(response.keys())}")
                elif isinstance(response, list) and len(response) > 0:
                    print(f"   Array length: {len(response)}")
                    if isinstance(response[0], dict):
                        print(f"   First item keys: {list(response[0].keys())}")
                        
            except Exception as e:
                results[endpoint] = {
                    "success": False, 
                    "error": str(e)
                }
                print(f"❌ {endpoint}: {str(e)}")
                
        return results
    '''
    
    print("=== Test Function to Add to ExtendedSession ===")
    print(test_code)
    
    return test_code

if __name__ == "__main__":
    potential_endpoints = explore_webuntis_api()
    create_test_function()
