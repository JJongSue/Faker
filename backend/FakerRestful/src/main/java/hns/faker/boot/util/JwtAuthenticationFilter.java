package hns.faker.boot.util;

import lombok.RequiredArgsConstructor;

import org.springframework.web.filter.GenericFilterBean;

import javax.servlet.FilterChain;
import javax.servlet.ServletException;
import javax.servlet.ServletRequest;
import javax.servlet.ServletResponse;
import javax.servlet.http.HttpServletRequest;
import java.io.IOException;

//@RequiredArgsConstructor
public class JwtAuthenticationFilter extends GenericFilterBean {
	
	
	private JwtTokenProvider jwtTokenProvider;

	public JwtAuthenticationFilter() {}

	public JwtAuthenticationFilter(JwtTokenProvider jwtTokenProvider2) {}

	@Override
	public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)
			throws IOException, ServletException {
		if(excludeUrl((HttpServletRequest)request)) {
			 chain.doFilter(request, response); //아닐경우 요청값 변경
		}else {
			
		}
//		HttpServletRequest httprequest= (HttpServletRequest)request;
//		 if(excludeUrl(httprequest)){
//			 chain.doFilter(request, response);//걸러내는 URI일 경우 요청값 그대로 처리
//			  }else{
//					// 헤더에서 JWT 를 받아옵니다.
//					String token = jwtTokenProvider.resolveToken((HttpServletRequest) request);
//					// 유효한 토큰인지 확인합니다.
//					if (token != null && jwtTokenProvider.validateToken(token)) {
//						// 토큰이 유효하면 토큰으로부터 유저 정보를 받아옵니다.
//						Authentication authentication = jwtTokenProvider.getAuthentication(token);
//						// SecurityContext 에 Authentication 객체를 저장합니다.
//						SecurityContextHolder.getContext().setAuthentication(authentication);
//					}
//			     chain.doFilter(request, response); //아닐경우 요청값 변경
//			  }

	}

	private boolean excludeUrl(HttpServletRequest request) {
		String uri = request.getRequestURI().toString().trim();
		System.out.println(uri);
		if (uri.startsWith("/swagger")||uri.startsWith("/webjars")||uri.startsWith("/v2")) {
			System.out.println("여긴가");
			return true;
		} else  {
			return false;
		}
	}

}
